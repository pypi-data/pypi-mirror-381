
from functools import reduce
import ufl
from ufl import grad, TrialFunction, SpatialCoordinate, FacetNormal,\
                Coefficient, conditional
from dune.source.cplusplus import Variable, UnformattedExpression,\
                                  AccessModifier, Declaration, Method
from .boundary import splitBoundary

def uflExpr(Model,space,t):
    u = TrialFunction(space)
    n = FacetNormal(space)
    x = SpatialCoordinate(space)

    physicalBound = None
    lowerBound = getattr(Model,"lowerBound",None)
    if lowerBound is None:
        lowerBound = space.dimRange*["std::numeric_limits<double>::min()"]
    else:
        lowerCond = [conditional(u[i]>=lowerBound[i],1,0)
                                  for i in range(len(lowerBound))
                                  if lowerBound[i] is not None ]
        if lowerCond != []:
            physicalBound = reduce( (lambda x,y: x*y), lowerCond )
        else: lowerBound=space.dimRange*["std::numeric_limits<double>::min()"]
    upperBound = getattr(Model,"upperBound",None)
    if upperBound is None:
        upperBound = space.dimRange*["std::numeric_limits<double>::max()"]
    else:
        upperCond = [conditional(u[i]<=upperBound[i],1,0)
                                  for i in range(len(upperBound))
                                  if upperBound[i] is not None ]
        if upperCond != []:
            physicalBound_ = reduce( (lambda x,y: x*y), upperCond )
            physicalBound = physicalBound_ if physicalBound is None else\
                            physicalBound*physicalBound_
        else: upperBound=space.dimRange*["std::numeric_limits<double>::min()"]

    maxWaveSpeed = getattr(Model,"maxWaveSpeed",None)
    # check for deprecated maxLambda
    if maxWaveSpeed is None:
        maxWaveSpeed = getattr(Model,"maxLambda",None)
        if maxWaveSpeed is not None:
            print("WARNING: maxLambda is deprecated, use maxWaveSpeed instead!")

    if maxWaveSpeed is not None:
        maxWaveSpeed = maxWaveSpeed(t,x,u,n)

    velocity = getattr(Model,"velocity",None)
    if velocity is not None:
        velocity = velocity(t,x,u)
    diffusionTimeStep = getattr(Model,"maxDiffusion",None)
    if diffusionTimeStep is not None:
        diffusionTimeStep = diffusionTimeStep(t,x,u)
    physical = getattr(Model,"physical",True)
    if not isinstance(physical,bool):
        physical = physical(t,x,u)
        if physicalBound is not None:
            physical = physical*physicalBound
    else:
        if physicalBound is not None:
            physical = physical*physicalBound
    # TODO: jump is problematic since the coefficient 'w' causes issues -
    # no predefined when extracting required Coefficients so needs fixing
    # So jump is not returned by this method and is constructed again in
    # the code generation process
    # w = Coefficient(space)
    jump = getattr(Model,"jump",None)
    if jump is not None:
        jump = jump(t,x,u,u)
    hasAdvFlux = hasattr(Model,"F_c")
    hasDiffFlux = hasattr(Model,"F_v")

    (
        boundaryAFlux,
        boundaryDFlux,
        boundaryValue,
        hasBoundaryValue,
    ) = splitBoundary(Model, t, x, u, n)

    limiterModifiedDict = getattr(Model,"limitedRange",None)
    if limiterModifiedDict is None:
        limiterModified = {}
        limitedDimRange = "DFunctionSpace :: dimRange"
    else:
        limiterModified = {}
        count = len(limiterModifiedDict.items())
        # for id,f in limiterModifiedDict.items(): count += 1
        limitedDimRange = str(count)
    # jump = None # TODO: see comment above
    return maxWaveSpeed, velocity, diffusionTimeStep, physical, jump,\
           boundaryAFlux, boundaryDFlux, boundaryValue, hasBoundaryValue,\
           physicalBound

def codeFemDg(self, *args, **kwargs):
    code = self._code( ellipticBndConditions = False )
    code.append(AccessModifier("public"))
    # TODO: why isn't this being used - see jump? Code duplication going on here...
    # velocity, maxWaveSpeed, velocity, diffusionTimeStep, physical, jump,\
    #        boundaryAFlux,boundaryDFlux,boundaryValues,hasBoundaryValues = self._patchExpr
    space = self._space
    Model = self._Model
    t = self._t

    u = TrialFunction(space)
    n = FacetNormal(space)
    x = SpatialCoordinate(space)

    physicalBound = None
    lowerBound = getattr(Model,"lowerBound",None)
    if lowerBound is None:
        lowerBound = space.dimRange*["std::numeric_limits<double>::min()"]
    else:
        lowerCond = [conditional(u[i]>=lowerBound[i],1,0)
                                  for i in range(len(lowerBound))
                                  if lowerBound[i] is not None ]
        if lowerCond != []:
            physicalBound = reduce( (lambda x,y: x*y), lowerCond )
        else: lowerBound=space.dimRange*["std::numeric_limits<double>::min()"]
    upperBound = getattr(Model,"upperBound",None)
    if upperBound is None:
        upperBound = space.dimRange*["std::numeric_limits<double>::max()"]
    else:
        upperCond = [conditional(u[i]<=upperBound[i],1,0)
                                  for i in range(len(upperBound))
                                  if upperBound[i] is not None ]
        if upperCond != []:
            physicalBound_ = reduce( (lambda x,y: x*y), upperCond )
            physicalBound = physicalBound_ if physicalBound is None else\
                            physicalBound*physicalBound_
        else: upperBound=space.dimRange*["std::numeric_limits<double>::min()"]

    # TODO come up with something better!
    hasGamma = getattr(Model,"gamma",None)
    code.append([Declaration(
                 Variable("constexpr bool", "hasGamma"), initializer=True if hasGamma else False,
                 static=True)])
    if hasGamma:
        try:
            code.append([Declaration(
                         Variable("constexpr double", "gamma"), initializer=Model.gamma(),
                         static=True)])
        except TypeError:
            code.append([Declaration(
                         Variable("constexpr double", "gamma"), initializer=Model.gamma,
                         static=True)])

    predefined = {}
    spatial = Variable('const auto', 'y')
    predefined.update( {x: UnformattedExpression('auto', 'entity.geometry().global( Dune::Fem::coordinate( x ) )') })
    arg_n = Variable("const DDomainType &", "normal")
    predefined.update( {n: arg_n} )
    arg_t = Variable("const double &", "t")
    predefined.update( {t: arg_t} )
    self.predefineCoefficients(predefined,'x')

    # pressure and temperature for potential temperature formulation
    pressureTemperature = getattr(Model,"pressureTemperature",None)
    if pressureTemperature is not None:
        pressureTemperature = pressureTemperature(u)
    self.generateMethod(code, pressureTemperature,
          'Dune::FieldVector<double, 2>', 'pressureTemperature',
          args=['const State &u'],
          targs=['class State'], const=True, inline=True,
          predefined=predefined)

    # background atmosphere
    background = getattr(Model,"background",None)
    if background is not None:
        background = background(t,x)
    self.generateMethod(code, background,
          'RRangeType', 'background',
          args=['const double &t',
                'const Entity &entity', 'const Point &x'],
          targs=['class Entity, class Point'], const=True, inline=True,
          predefined=predefined)

    maxWaveSpeed = getattr(Model,"maxWaveSpeed",None)
    # check for deprecated maxLambda
    if maxWaveSpeed is None:
        maxWaveSpeed = getattr(Model,"maxLambda",None)
        if maxWaveSpeed is not None:
            print("WARNING: maxLambda is deprecated, use maxWaveSpeed instead!")

    if maxWaveSpeed is not None:
        maxWaveSpeed = maxWaveSpeed(t,x,u,n)

    self.generateMethod(code, maxWaveSpeed,
            'double', 'maxWaveSpeed',
            args=['const double &t',
                  'const Entity &entity', 'const Point &x',
                  'const DDomainType &normal',
                  'const DRangeType &u'],
            targs=['class Entity, class Point'], const=True, inline=True,
            predefined=predefined)

    velocity = getattr(Model,"velocity",None)
    if velocity is not None:
        velocity = velocity(t,x,u)
    self.generateMethod(code, velocity,
            'DDomainType', 'velocity',
            args=['const double &t',
                  'const Entity &entity', 'const Point &x',
                  'const DRangeType &u'],
            targs=['class Entity, class Point'], const=True,inline=True,
            predefined=predefined)

    # TODO: fill in diffusion time step from Model
    diffusionTimeStep = getattr(Model,"maxDiffusion",None)
    if diffusionTimeStep is not None:
        diffusionTimeStep = diffusionTimeStep(t,x,u)
    self.generateMethod(code, diffusionTimeStep,
            'double', 'diffusionTimeStep',
            args=['const Entity& entity', 'const Point &x', 'const DRangeType &u'],
            targs=['class Entity, class Point'], const=True,inline=True,
            predefined=predefined)

    hasPhysical = hasattr(Model,"physical")
    # add static variable for hasPhysical
    code.append([Declaration(
                 Variable("constexpr bool", "hasPhysical"), initializer=hasPhysical,
                 static=True)])

    physical = getattr(Model,"physical",True)
    if not isinstance(physical,bool):
        physical = physical(t,x,u)
        if physicalBound is not None:
            physical = physical*physicalBound
    else:
        if physicalBound is not None:
            physical = physical*physicalBound

    # add method physical
    self.generateMethod(code, physical,
            'double', 'physical',
            args=['const Entity &entity', 'const Point &x',
                  'const DRangeType &u'],
            targs=['class Entity, class Point'],
            const=True,inline=True,
            predefined=predefined)

    w = Coefficient(space)
    jmpPredefined = predefined.copy()
    jmpPredefined.update( {w:Variable("const DRangeType &", "w")} )
    jmpPredefined.update( {x: UnformattedExpression('auto', 'it.geometry().global( Dune::Fem::coordinate( x ) )') })
    jump = getattr(Model,"jump",None)
    if jump is not None:
        jump = jump(t,x,u,w)
    self.generateMethod(code, jump,
            'double', 'jump',
            args=['const Intersection& it', 'const Point &x',
                  'const DRangeType &u',
                  'const DRangeType &w'],
            targs=['class Intersection, class Point'], const=True,inline=True,
            predefined=jmpPredefined)

    # still missing
    adjustAverageValue = {}
    self.generateMethod(code, adjustAverageValue,
            'void', 'adjustAverageValue',
            args=['const Entity& entity', 'const Point &x',
                  'DRangeType &u'],
            targs=['class Entity, class Point'], const=True,evalSwitch=False,inline=True,
            predefined=predefined)

    hasAdvFlux = hasattr(Model,"F_c")
    hasDiffFlux = hasattr(Model,"F_v")
    #####################
    ## boundary treatment
    # TODO make 'copy' boundary conditions the default?
    (
        boundaryAFlux,
        boundaryDFlux,
        boundaryValue,
        hasBoundaryValue,
    ) = splitBoundary(Model, t, x, u, n)

    self.generateMethod(code, boundaryAFlux,
            'bool', 'boundaryFlux',
            args=['const int bndId',
                  'const double &t',
                  'const Entity& entity', 'const Point &x',
                  'const DDomainType &normal',
                  'const DRangeType &u',
                  'RRangeType &result'],
            targs=['class Entity, class Point'], const=True,inline=True,
            predefined=predefined)
    self.generateMethod(code, boundaryDFlux,
            'bool', 'diffusionBoundaryFlux',
            args=['const int bndId',
                  'const double &t',
                  'const Entity& entity', 'const Point &x',
                  'const DDomainType &normal',
                  'const DRangeType &u',
                  'const DJacobianRangeType &jac',
                  'RRangeType &result'],
            targs=['class Entity, class Point'], const=True,inline=True,
            predefined=predefined)

    self.generateMethod(code, hasBoundaryValue,
            'bool', 'hasBoundaryValue',
            args=['const int bndId',
                  'const double &t',
                  'const Entity& entity', 'const Point &x',
                  'const DRangeType &u',
                  'RRangeType &result'],
            targs=['class Entity, class Point'], const=True,inline=True,
            predefined=predefined)
    self.generateMethod(code, boundaryValue,
            'bool', 'boundaryValue',
            args=['const int bndId',
                  'const double &t',
                  'const Entity& entity', 'const Point &x',
                  'const DDomainType &normal',
                  'const DRangeType &u',
                  'RRangeType &result'],
            targs=['class Entity, class Point'], const=True,inline=True,
            predefined=predefined)

    limiterModifiedDict = getattr(Model,"limitedRange",None)
    if limiterModifiedDict is None:
        limiterModified = {}
        limitedDimRange = "DFunctionSpace :: dimRange"
    else:
        limiterModified = {}
        count = len(limiterModifiedDict.items())
        # for id,f in limiterModifiedDict.items(): count += 1
        limitedDimRange = str(count)
    self.generateMethod(code, limiterModified,
            'void', 'limitedRange',
            args=['LimitedRange& limRange'],
            targs=['class LimitedRange'], const=True, evalSwitch=False,inline=True,
            predefined=predefined)
    obtainBounds = Method("void","obtainBounds",
                          targs=['class LimitedRange'],
                          args=["LimitedRange& globalMin","LimitedRange& globalMax"],const=True)
    obtainBounds.append("globalMin = {"
                        + ', '.join(map(str, lowerBound))
                        +"};")
    obtainBounds.append("globalMax = {"
                        + ', '.join(map(str, upperBound))
                        +"};")
    code.append( [obtainBounds] )
    return code

def transform(Model,space,t, name="" ):
    allExpr = uflExpr(Model,space,t)
    def transform_(model):
        if model.baseName == "modelFemDg"+name:
            return
        model._code = model.code
        model.code  = lambda *args,**kwargs: codeFemDg(*args,**kwargs)
        model.baseName = "modelFemDg"+name
        model._Model = Model
        model._space = space
        model._t = t
        model._patchExpr = allExpr
        # model.modelWrapper = "DiffusionModelWrapper< Model >"
    retExpr  = [x for x in allExpr if not isinstance(x,(int,float,dict,list)) and x is not None]
    retExpr += [x for d in allExpr if isinstance(d,(dict,list))
                  for x in d.values() if not isinstance(x,(int,float,dict,list)) and x is not None]
    return [transform_, retExpr]
