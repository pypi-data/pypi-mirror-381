import logging, io
logger = logging.getLogger(__name__)
import numpy as np
from matplotlib import pyplot as plt

from ufl.equation import Equation
from ufl import Form
from dune.generator import Constructor, Method, algorithm
import dune
import dune.fem

def stabilization(spc, hessStabilization=None, gradStabilization=None, massStabilization=None):
    if hessStabilization is None and gradStabilization is None and massStabilization is None:
        gradStabilization = 1.
    if hessStabilization is None:
        hessStabilization = 0.
    else:
        hessStabilization = float(hessStabilization)
    if gradStabilization is None:
        gradStabilization = 0.
    else:
        gradStabilization = float(gradStabilization)
    if massStabilization is None:
        massStabilization = 0.
    else:
        massStabilization = float(massStabilization)
    if spc._stab is None:
        stabMatrix = dune.fem.operator.linear([spc,spc])
        spc._stab = algorithm.load("Dune::Vem::stabilization",
           io.StringIO("#include <dune/vem/operator/stabmatrix.hh>"), stabMatrix,
                       hessStabilization,gradStabilization,massStabilization)
    else:
        stabMatrix = dune.fem.operator.linear([spc,spc])
    spc._stab(stabMatrix, hessStabilization, gradStabilization, massStabilization)
    return stabMatrix


def bbdgSpace(view, order=1, scalar=False, dimRange=None, field="double",
             rotatedBB=True,
             storage="numpy"):
    """create a discontinous galerkin space over an agglomerated grid

    Args:
        view: the underlying grid view
        order: polynomial order of the finite element functions
        dimRange: dimension of the range space
        field: field of the range space
        storage: underlying linear algebra backend

    Returns:
        Space: the constructed Space
    """

    from dune.fem.space import module, addStorage
    if dimRange is None:
        dimRange = 1
        scalar = True

    if dimRange > 1 and scalar:
        raise KeyError(\
                "trying to set up a scalar space with dimRange = " +\
                str(dimRange) + ">1")
    if dimRange < 1:
        raise KeyError(\
            "Parameter error in BBDGSpace with "+
            "dimRange=" + str(dimRange) + ": " +\
            "dimRange has to be greater or equal to 1")
    if order < 0:
        raise KeyError(\
            "Parameter error in BBDGSpace with "+
            "order=" + str(order) + ": " +\
            "order has to be greater or equal to 0")
    if field == "complex":
        field = "std::complex<double>"

    agglomerate = view.hierarchicalGrid.agglomerate

    includes = [ "dune/vem/agglomeration/dgspace.hh" ] + view.cppIncludes
    dimw = view.dimWorld
    viewType = view.cppTypeName

    gridPartName = "Dune::FemPy::GridPart< " + view.cppTypeName + " >"
    typeName = "Dune::Vem::AgglomerationDGSpace< " +\
      "Dune::Fem::FunctionSpace< double, " + field + ", " + str(dimw) + ", " + str(dimRange) + " >, " +\
      gridPartName + ", " + str(order) + " >"

    constructor = Constructor(
                   ['pybind11::handle gridView',
                    'const pybind11::object agglomerate',
                    'bool rotatedBB'],
                   ['typedef Dune::Vem::Agglomeration<' + gridPartName + '> AggloType;',
                    'AggloType *agglo = nullptr;',
                    '// check storage',
                    'pybind11::function retrieve = pybind11::module::import("dune.vem.vem").attr("retrieveAgglo_");',
                    'pybind11::function insert   = pybind11::module::import("dune.vem.vem").attr("insertAgglo_");',
                    'pybind11::function remove   = pybind11::module::import("dune.vem.vem").attr("removeAgglo_");',
                    'pybind11::handle aggloExists = retrieve(gridView);',
                    'if (! pybind11::isinstance<pybind11::none>(aggloExists) ) {',
                    '  agglo = static_cast<AggloType*>(aggloExists.cast<void*>());',
                    '}',
                    'else {',
                    '  agglo = new AggloType(',
                    '           Dune::FemPy::gridPart<' + viewType + '>(gridView),rotatedBB,',
                    '      [agglomerate](const auto& idx)',
                    '      { return agglomerate(idx).template cast<unsigned int>(); } );',
                    '  insert(gridView,(void*)agglo);',
                    '  pybind11::cpp_function aggloCleanup(',
                    '        [agglo,remove](pybind11::handle weakref) {',
                    '        remove((void*)agglo);',
                    '        delete agglo;',
                    '        weakref.dec_ref();',
                    '    });',
                    '  (void) pybind11::weakref(gridView, aggloCleanup).release();',
                    '}',
                    'auto obj = new DuneType( *agglo );',
                    'return obj;'],
                   ['"gridView"_a', '"agglomerate"_a', '"rotatedBB"_a',
                    'pybind11::keep_alive< 1, 2 >()'] )


    # is defined on the index set which is not used for the dg space
    # diameterMethod = Method('diameters',
    #    '''[]( DuneType &self ) { return self.blockMapper().indexSet().diameters(); }''' )
    updateMethod = Method('update',
       '''[]( DuneType &self ) { self.update(); }''' )

    spc = module(field, includes, typeName, constructor, updateMethod, scalar=scalar, storage=storage,
             ctorArgs=[view, agglomerate,rotatedBB])
    addStorage(spc, storage)
    return spc.as_ufl()

from dune.fem.scheme import dg
def bbdgScheme(model, space=None, penalty=1, solver=None, parameters={}):
    if space == None:
        try:
            space = model.lhs.arguments()[0].ufl_function_space()
        except AttributeError:
            raise ValueError("no space provided and could not deduce from form provided")
    spaceType = space.cppTypeName
    penaltyClass = "Dune::Vem::BBDGPenalty<"+spaceType+">"
    return dg(model,space,penalty,solver,parameters,penaltyClass)
    # return galerkin(model,space,solver,parameters)

def vemSpace(view, order=1, orderTuple=None,
             testSpaces=None, scalar=False,
             dimRange=None, conforming=True, field="double",
             storage="numpy",
             basisChoice=2, rotatedBB=True,
             edgeInterpolation=False,
             vectorSpace=False, reduced=False,
             basisField="double", computeField="long double",
             gradProjectionWithIByParts=False
             ):
    """create a virtual element space over an agglomerated grid

    Args:
        view: the underlying grid view
        order: polynomial order of the finite element functions
        dimRrange: dimension of the range space
        field: field of the range space
        storage: underlying linear algebra backend

    Returns:
        Space: the constructed Space
    """
    if orderTuple is None:
        try:
            orderTuple = order
            order = orderTuple[0]
        except TypeError:
            orderTuple = [-1,-1,-1]

    assert order >= 1

    if gradProjectionWithIByParts:
        useNewGradProjection = ["NEWGRADPROJECTION"]
    else:
        useNewGradProjection = []

    from dune.fem.space import module, addStorage
    if dimRange is None:
        dimRange = 1
        scalar = True

    if dimRange > 1 and scalar:
        raise KeyError(\
                "trying to set up a scalar space with dimRange = " +\
                str(dimRange) + ">1")
    if dimRange < 1:
        raise KeyError(\
            "Parameter error in vemSpace with "+
            "dimRange=" + str(dimRange) + ": " +\
            "dimRange has to be greater or equal to 1")
    if order < 0:
        raise KeyError(\
            "Parameter error in vemSpace with "+
            "order=" + str(order) + ": " +\
            "order has to be greater or equal to 0")
    if field == "complex":
        field = "std::complex<double>"

    if testSpaces is None:
        if conforming:
            testSpaces = [  [0], [order-2], [order-2] ]
        else:
            testSpaces = [ [-1], [order-1], [order-2] ]
    if testSpaces == "serendipity":
        etaMin = view.hierarchicalGrid.agglomerate.minEdgeNumber
        testSpaces = [  [0], [order-2], [max(-1,order-etaMin)] ]
        print("serendipity:",testSpaces,etaMin)

    for i,ts in enumerate(testSpaces):
        if type(ts) == int:
            testSpaces[i] = [ts]

    try:
        agglomerate = view.hierarchicalGrid.agglomerate
    except AttributeError:
        # if view does not have agglomerate then we create a trivial one
        # this only works for quads or triangles
        view.hierarchicalGrid.agglomerate = TrivialAgglomerate(view)
        agglomerate = view.hierarchicalGrid.agglomerate

    includes = [ "dune/fem/gridpart/common/gridpart.hh", "dune/vem/space/hk.hh" ] + view.cppIncludes
    dimw = view.dimWorld
    viewType = view.cppTypeName

    gridPartName = "Dune::FemPy::GridPart< " + view.cppTypeName + " >"
    typeName = "Dune::Vem::AgglomerationVEMSpace< " +\
      "Dune::Fem::FunctionSpace< double, " + field + ", " + str(dimw) + ", " + str(dimRange) + " >, " +\
      gridPartName +\
      (", true " if vectorSpace else ", false ") +\
      (", true " if reduced else ", false ") +\
      ", " + basisField + ", " + computeField +\
      " >"
    constructor = Constructor(
                   ['pybind11::handle gridView',
                    'const pybind11::object agglomerate',
                    'unsigned int order',
                    'const std::array<int,3> orderTuple',
                    'const std::array<std::vector<int>,'+str(view.dimension+1)+'> &testSpaces',
                    'int basisChoice','bool edgeInterpolation','bool rotatedBB'],
                   ['typedef Dune::Vem::Agglomeration<' + gridPartName + '> AggloType;',
                    'AggloType *agglo = nullptr;',
                    '// check storage',
                    'pybind11::function retrieve = pybind11::module::import("dune.vem.vem").attr("retrieveAgglo_");',
                    'pybind11::function insert   = pybind11::module::import("dune.vem.vem").attr("insertAgglo_");',
                    'pybind11::function remove   = pybind11::module::import("dune.vem.vem").attr("removeAgglo_");',
                    'pybind11::handle aggloExists = retrieve(gridView);',
                    'if (! pybind11::isinstance<pybind11::none>(aggloExists) ) {',
                    '  // std::cout << "retrieve agglo\\n";',
                    '  agglo = static_cast<AggloType*>(aggloExists.cast<void*>());',
                    '}',
                    'else {',
                    '  agglo = new AggloType(',
                    '           Dune::FemPy::gridPart<' + viewType + '>(gridView),rotatedBB,',
                    '      [agglomerate](const auto& idx)',
                    '      { return agglomerate(idx).template cast<unsigned int>(); } );',
                    '  insert(gridView,(void*)agglo);',
                    '  pybind11::cpp_function aggloCleanup(',
                    '        [agglo,remove](pybind11::handle weakref) {',
                    '        // std::cout << "remove agglo\\n";',
                    '        remove((void*)agglo);',
                    '        delete agglo;',
                    '        weakref.dec_ref();',
                    '    });',
                    '  (void) pybind11::weakref(gridView, aggloCleanup).release();',
                    '  // std::cout << "new agglo\\n";',
                    '}',
                    'auto obj = new DuneType(*agglo, order, orderTuple, testSpaces, basisChoice, edgeInterpolation );',
                    'return obj;'],
                   ['"gridView"_a', '"agglomerate"_a',
                    '"order"_a',
                    '"orderTuple"_a',
                    '"testSpaces"_a',
                    '"basisChoice"_a', '"edgeInterpolation"_a', '"rotatedBB"_a',
                    'pybind11::keep_alive< 1, 2 >()'] )
    diameterMethod = Method('diameters',
       '''[]( DuneType &self ) { return self.blockMapper().indexSet().diameters(); }''' )
    updateMethod = Method('update',
       '''[]( DuneType &self ) { self.update(); }''' )

    from dune.fem.space import _defaultGenerator
    class NewGenerator:
        def __init__(self):
            pass
        def load(self,*args,**kwargs):
            kwargs["defines"] = kwargs.get("defines",[]) + useNewGradProjection
            return _defaultGenerator.load(*args,**kwargs)

    spc = module(field, includes, typeName, constructor, diameterMethod, updateMethod,
                generator = NewGenerator(),
                scalar=scalar, storage=storage,
                ctorArgs=[view, agglomerate, order, orderTuple, testSpaces, basisChoice, edgeInterpolation, rotatedBB])
    addStorage(spc, storage)

    spc._stab = None
    spc.__class__.stabilization = stabilization

    return spc.as_ufl()

def space(view, order=1, dimRange=None,
          testSpaces=None,
          conforming=True,
          version=None,
          scalar=False,
          basisChoice=2,
          field="double", storage="numpy"):
    '''
        version is tuple,list for a general vem space (=tests[aces)
        version == "dg" (bbdg)
        version == "dgSimplex" (dg on triangulation)
        version == "continuous" (vem)
        version == "continuousSimplex" (lagrange)
        version == "non-conformin" (vem)
    '''
    if version is None and testSpaces is None:
        raise AttributeError("version and testSpaces parameters can not both be None (default)")
    if version is None: version = testSpaces
    if isinstance(version,tuple) or isinstance(version,list):
        return vemSpace(view,order=order,scalar=scalar,dimRange=dimRange,field=field,storage=storage,
                        testSpaces=version, basisChoice=basisChoice)
    elif version == "dg":
        return bbdgSpace(view,order=order,scalar=scalar,dimRange=dimRange,field=field,storage=storage)
    elif version == "dgSimplex":
        from dune.fem.space import onb
        return onb(view,order=order,scalar=scalar,dimRange=dimRange,field=field,storage=storage)
    elif version == "continuous":
        return vemSpace(view,order=order,scalar=scalar,dimRange=dimRange,field=field,storage=storage,
                        conforming=True, basisChoice=basisChoice)
    elif version == "continuousSimplex":
        from dune.fem.space import lagrange
        return lagrange(view,order=order,scalar=scalar,dimRange=dimRange,field=field,storage=storage)
    elif version == "non-conforming":
        return vemSpace(view,order=order,scalar=scalar,dimRange=dimRange,field=field,storage=storage,
                        conforming=False, basisChoice=basisChoice)
    raise AttributeError("wrong version string provided:",version)

###############################

def curlFreeSpace(view, order=1,
             field="double", storage="numpy",
             basisChoice=2, rotatedBB=True):
    """create a virtual element space over an agglomerated grid

    Args:
        view: the underlying grid view
        order: polynomial order of the finite element functions
        field: field of the range space
        storage: underlying linear algebra backend

    Returns:
        Space: the constructed Space
    """

    from dune.fem.space import module, addStorage

    if order < 0:
        raise KeyError(\
            "Parameter error in curlFreeSpace with "+
            "order=" + str(order) + ": " +\
            "order has to be greater or equal to 0")

    agglomerate = view.hierarchicalGrid.agglomerate

    includes = [ "dune/fem/gridpart/common/gridpart.hh", "dune/vem/space/curlfree.hh" ] + view.cppIncludes
    dimw = view.dimWorld
    viewType = view.cppTypeName

    gridPartName = "Dune::FemPy::GridPart< " + view.cppTypeName + " >"
    typeName = "Dune::Vem::CurlFreeVEMSpace< " + gridPartName + " >"
    constructor = Constructor(
                   ['pybind11::handle gridView',
                    'const pybind11::object agglomerate',
                    'unsigned int order',
                    'int basisChoice','bool rotatedBB'],
                   ['typedef Dune::Vem::Agglomeration<' + gridPartName + '> AggloType;',
                    'AggloType *agglo = nullptr;',
                    '// check storage',
                    'pybind11::function retrieve = pybind11::module::import("dune.vem.vem").attr("retrieveAgglo_");',
                    'pybind11::function insert   = pybind11::module::import("dune.vem.vem").attr("insertAgglo_");',
                    'pybind11::function remove   = pybind11::module::import("dune.vem.vem").attr("removeAgglo_");',
                    'pybind11::handle aggloExists = retrieve(gridView);',
                    'if (! pybind11::isinstance<pybind11::none>(aggloExists) ) {',
                    '  // std::cout << "retrieve agglo\\n";',
                    '  agglo = static_cast<AggloType*>(aggloExists.cast<void*>());',
                    '}',
                    'else {',
                    '  agglo = new AggloType(',
                    '           Dune::FemPy::gridPart<' + viewType + '>(gridView),rotatedBB,',
                    '      [agglomerate](const auto& idx)',
                    '      { return agglomerate(idx).template cast<unsigned int>(); } );',
                    '  insert(gridView,(void*)agglo);',
                    '  pybind11::cpp_function aggloCleanup(',
                    '        [agglo,remove](pybind11::handle weakref) {',
                    '        // std::cout << "remove agglo\\n";',
                    '        remove((void*)agglo);',
                    '        delete agglo;',
                    '        weakref.dec_ref();',
                    '    });',
                    '  (void) pybind11::weakref(gridView, aggloCleanup).release();',
                    '  // std::cout << "new agglo\\n";',
                    '}',
                    'auto obj = new DuneType(*agglo, order, basisChoice );',
                    'return obj;'],
                   ['"gridView"_a', '"agglomerate"_a',
                    '"order"_a',
                    '"basisChoice"_a', '"rotatedBB"_a',
                    'pybind11::keep_alive< 1, 2 >()'] )
    diameterMethod = Method('diameters',
       '''[]( DuneType &self ) { return self.blockMapper().indexSet().diameters(); }''' )
    updateMethod = Method('update',
       '''[]( DuneType &self ) { self.update(); }''' )

    spc = module(field, includes, typeName, constructor, diameterMethod, updateMethod,
                storage=storage,
                ctorArgs=[view, agglomerate, order, basisChoice, rotatedBB])
    addStorage(spc, storage)
    spc._stab = None
    spc.stabilization = lambda: stabilization(spc)
    return spc.as_ufl()

#########################################################

def divFreeSpace(view, order=2, conforming=True,
             field="double", storage="numpy",
             basisChoice=2, edgeInterpolation=False, rotatedBB=True):
    """create a virtual element space over an agglomerated grid

    Args:
        view: the underlying grid view
        order: polynomial order of the finite element functions
        field: field of the range space
        storage: underlying linear algebra backend

    Returns:
        Space: the constructed Space
    """

    from dune.fem.space import module, addStorage

    if order < 2:
        raise KeyError(\
            "Parameter error in divFreeSpace with "+
            "order=" + str(order) + ": " +\
            "order has to be greater or equal to 2")

    agglomerate = view.hierarchicalGrid.agglomerate

    includes = [ "dune/fem/gridpart/common/gridpart.hh", "dune/vem/space/divfree.hh" ] + view.cppIncludes
    dimw = view.dimWorld
    viewType = view.cppTypeName

    gridPartName = "Dune::FemPy::GridPart< " + view.cppTypeName + " >"
    typeName = "Dune::Vem::DivFreeVEMSpace< " + gridPartName + " >"
    constructor = Constructor(
                   ['pybind11::handle gridView',
                    'const pybind11::object agglomerate',
                    'unsigned int order', 'bool conforming',
                    'int basisChoice','bool edgeInterpolation','bool rotatedBB'],
                   ['typedef Dune::Vem::Agglomeration<' + gridPartName + '> AggloType;',
                    'AggloType *agglo = nullptr;',
                    '// check storage',
                    'pybind11::function retrieve = pybind11::module::import("dune.vem.vem").attr("retrieveAgglo_");',
                    'pybind11::function insert   = pybind11::module::import("dune.vem.vem").attr("insertAgglo_");',
                    'pybind11::function remove   = pybind11::module::import("dune.vem.vem").attr("removeAgglo_");',
                    'pybind11::handle aggloExists = retrieve(gridView);',
                    'if (! pybind11::isinstance<pybind11::none>(aggloExists) ) {',
                    '  // std::cout << "retrieve agglo\\n";',
                    '  agglo = static_cast<AggloType*>(aggloExists.cast<void*>());',
                    '}',
                    'else {',
                    '  agglo = new AggloType(',
                    '           Dune::FemPy::gridPart<' + viewType + '>(gridView),rotatedBB,',
                    '      [agglomerate](const auto& idx)',
                    '      { return agglomerate(idx).template cast<unsigned int>(); } );',
                    '  insert(gridView,(void*)agglo);',
                    '  pybind11::cpp_function aggloCleanup(',
                    '        [agglo,remove](pybind11::handle weakref) {',
                    '        // std::cout << "remove agglo\\n";',
                    '        remove((void*)agglo);',
                    '        delete agglo;',
                    '        weakref.dec_ref();',
                    '    });',
                    '  (void) pybind11::weakref(gridView, aggloCleanup).release();',
                    '  // std::cout << "new agglo\\n";',
                    '}',
                    'auto obj = new DuneType(*agglo, order, conforming, basisChoice, edgeInterpolation );',
                    'return obj;'],
                   ['"gridView"_a', '"agglomerate"_a',
                    '"order"_a', '"conforming"_a',
                    '"basisChoice"_a', '"edgeInterpolation"_a','"rotatedBB"_a',
                    'pybind11::keep_alive< 1, 2 >()'] )
    diameterMethod = Method('diameters',
       '''[]( DuneType &self ) { return self.blockMapper().indexSet().diameters(); }''' )
    updateMethod = Method('update',
       '''[]( DuneType &self ) { self.update(); }''' )

    spc = module(field, includes, typeName, constructor, diameterMethod, updateMethod,
                storage=storage,
                ctorArgs=[view, agglomerate, order, conforming, basisChoice, edgeInterpolation, rotatedBB])
    addStorage(spc, storage)
    spc._stab = None
    spc.stabilization = lambda: stabilization(spc)
    return spc.as_ufl()

#########################################################
#########################################################

# from dune.fem.model import elliptic
from dune.fem.model import integrands
from dune.vem.patch import transform
from dune.fem.model import warnNewCartesianIds

def vemModel(view, equation, space,
        hessStabilization=None,gradStabilization=None, massStabilization=None,
        *args, **kwargs):
    warnNewCartesianIds(view,*args)
    return integrands(view, equation,
                      modelPatch=transform(space,hessStabilization,gradStabilization,massStabilization),
                      includes=["dune/vem/py/integrands.hh"],
                      *args, **kwargs)

def vemScheme(model, space=None, solver=None, parameters={},
              hessStabilization=None, gradStabilization=None, massStabilization=None,
              boundary="default"):
    """create a scheme for solving second order pdes with the virtual element method

    Args:

    Returns:
        Scheme: the constructed scheme
    """

    from dune.fem.scheme import module
    from dune.fem.scheme import femschemeModule

    assert boundary == "default" or boundary=="full" or boundary=="value" or boundary=="derivative" or boundary is None

    modelParam = None
    if isinstance(model, (list, tuple)):
        modelParam = model[1:]
        model = model[0]
    if isinstance(model,Equation):
        if space == None:
            try:
                space = model.lhs.arguments()[0].ufl_function_space()
            except AttributeError:
                raise ValueError("no space provided and could not deduce from form provided")
        else:
            try:
                eqSpace = model.lhs.arguments()[0].ufl_function_space()
                if not eqSpace.dimRange == space.dimRange:
                    raise ValueError("""range of space used for arguments in equation
                    and the range of space passed to the scheme have to match -
                    space argument to scheme can be 'None'""")
            except AttributeError:
                pass
        if modelParam:
            model = vemModel(space.gridView,model,space,hessStabilization,gradStabilization,massStabilization,*modelParam)
        else:
            model = vemModel(space.gridView,model,space,hessStabilization,gradStabilization,massStabilization)

    includes = [ "dune/vem/operator/vemelliptic.hh", "dune/vem/operator/diffusionmodel.hh" ]

    op = lambda linOp,model: "DifferentiableVEMEllipticOperator< " +\
                             ",".join([linOp,model]) + ">"

    if model.hasDirichletBoundary:
        if boundary == "default": boundary = "full"
        assert boundary is not None
        includes += [ "dune/fem/schemes/dirichletwrapper.hh",
                      "dune/vem/operator/vemdirichletconstraints.hh"]
        if boundary   == "full":       boundary = 3
        elif boundary == "value":      boundary = 1
        elif boundary == "derivative": boundary = 2
        constraints = lambda model: "Dune::VemDirichletConstraints< " +\
                    ",".join([model,space.cppTypeName,'true',str(boundary)]) + " > "
        operator = lambda linOp,model: "DirichletWrapperOperator< " +\
                ",".join([op(linOp,model),constraints(model)]) + " >"
    else:
        assert boundary is None or boundary == "default"
        operator = op
    """
    elif boundary == 'derivative':
        includes += [ "dune/fem/schemes/dirichletwrapper.hh",
                      "dune/vem/operator/vemdirichletconstraints.hh"]
        constraints = lambda model: "Dune::VemDirichletConstraints< " +\
                    ",".join([model,space.cppTypeName,'true',str(2)]) + " > "
        operator = lambda linOp,model: "DirichletWrapperOperator< " +\
                ",".join([op(linOp,model),constraints(model)]) + " >"
    """

    spaceType = space.cppTypeName
    includes += ["dune/vem/operator/diffusionmodel.hh"]
    valueType = 'std::tuple< typename ' + spaceType + '::RangeType, typename ' + spaceType + '::JacobianRangeType >'
    modelType = 'Dune::Fem::VirtualizedVemIntegrands< typename ' + spaceType + '::GridPartType, ' + model._domainValueType + ", " + model._rangeValueType+ ' >'

    return femschemeModule(space,model,includes,solver,operator,
            parameters=parameters,
            modelType=modelType
            )


def vemOperator(model, domainSpace=None, rangeSpace=None, boundary="default"):
    # from dune.fem.model._models import elliptic as makeElliptic
    from dune.fem.operator import load
    if rangeSpace is None:
        rangeSpace = domainSpace

    modelParam = None
    if isinstance(model, (list, tuple)):
        modelParam = model[1:]
        model = model[0]
    if isinstance(model,Form):
        model = model == 0
    if isinstance(model,Equation):
        if rangeSpace == None:
            try:
                rangeSpace = model.lhs.arguments()[0].ufl_function_space()
            except AttributeError:
                raise ValueError("no range space provided and could not deduce from form provided")
        if domainSpace == None:
            try:
                domainSpace = model.lhs.arguments()[1].ufl_function_space()
            except AttributeError:
                raise ValueError("no domain space provided and could not deduce from form provided")
        if modelParam:
            model = vemModel(domainSpace.gridView,model,domainSpace,None,None,None,*modelParam)
        else:
            model = vemModel(domainSpace.gridView,model,domainSpace,None,None,None)

    if not hasattr(rangeSpace,"interpolate"):
        raise ValueError("wrong range space")
    if not hasattr(domainSpace,"interpolate"):
        raise ValueError("wrong domain space")

    domainSpaceType = domainSpace.cppTypeName
    rangeSpaceType = rangeSpace.cppTypeName

    storage,  domainFunctionIncludes, domainFunctionType, _, _, dbackend = domainSpace.storage
    rstorage, rangeFunctionIncludes,  rangeFunctionType,  _, _, rbackend = rangeSpace.storage
    if not rstorage == storage:
        raise ValueError("storage for both spaces must be identical to construct operator")

    includes = ["dune/vem/operator/vemelliptic.hh",
                "dune/fempy/py/grid/gridpart.hh",
                "dune/fem/schemes/dirichletwrapper.hh",
                "dune/vem/operator/vemdirichletconstraints.hh"]
    includes += domainSpace.cppIncludes + domainFunctionIncludes
    includes += rangeSpace.cppIncludes + rangeFunctionIncludes
    includes += ["dune/vem/operator/diffusionmodel.hh", "dune/fempy/parameter.hh"]

    import dune.create as create
    linearOperator = create.discretefunction(storage)(domainSpace,rangeSpace)[3]

    modelType = "VEMDiffusionModel< " +\
          "typename " + domainSpaceType + "::GridPartType, " +\
          domainSpaceType + "::dimRange, " +\
          rangeSpaceType + "::dimRange, " +\
          "typename " + domainSpaceType + "::RangeFieldType >"
    typeName = "DifferentiableVEMEllipticOperator< " + linearOperator + ", " + modelType + ">"
    if model.hasDirichletBoundary:
        if boundary == "default": boundary = "full"
        assert boundary is not None
        includes += [ "dune/fem/schemes/dirichletwrapper.hh",
                      "dune/vem/operator/vemdirichletconstraints.hh"]
        if boundary   == "full":       boundary = 3
        elif boundary == "value":      boundary = 1
        elif boundary == "derivative": boundary = 2

        useIdentity = 'true' if rangeSpace == domainSpace else 'false'
        constraints = lambda model: "Dune::VemDirichletConstraints< " +\
                    ",".join([model,rangeSpace.cppTypeName,useIdentity,str(boundary)]) + " > "
        typeName = "DirichletWrapperOperator< " +\
                ",".join([typeName,constraints(modelType)]) + " >"

    constructor = Constructor(['const '+domainSpaceType+'& dSpace','const '+rangeSpaceType+' &rSpace', modelType + ' &model'],
                              ['return new ' + typeName + '( dSpace, rSpace, model );'],
                              ['pybind11::keep_alive< 1, 2 >()', 'pybind11::keep_alive< 1, 3 >()', 'pybind11::keep_alive< 1, 4 >()'])

    scheme = load(includes, typeName, constructor).Operator(domainSpace,rangeSpace, model)
    scheme.model = model
    return scheme

#################################################################

def aluGrid(constructor, dimgrid=None, dimworld=None, elementType=None, **parameters):
    if not dimgrid:
        dimgrid = getDimgrid(constructor)
    if dimworld is None:
        dimworld = dimgrid
    if elementType is None:
        elementType = parameters.pop("type")
    refinement = parameters["refinement"]
    if refinement == "conforming":
        refinement="Dune::conforming"
    elif refinement == "nonconforming":
        refinement="Dune::nonconforming"
    if not (2 <= dimworld and dimworld <= 3):
        raise KeyError("Parameter error in ALUGrid with dimworld=" + str(dimworld) + ": dimworld has to be either 2 or 3")
    if not (2 <= dimgrid and dimgrid <= dimworld):
        raise KeyError("Parameter error in ALUGrid with dimgrid=" + str(dimgrid) + ": dimgrid has to be either 2 or 3")
    if refinement=="Dune::conforming" and elementType=="Dune::cube":
        raise KeyError("Parameter error in ALUGrid with refinement=" + refinement + " and type=" + elementType + ": conforming refinement is only available with simplex element type")
    typeName = "Dune::ALUGrid< " + str(dimgrid) + ", " + str(dimworld) + ", " + elementType + ", " + refinement + " >"
    includes = ["dune/alugrid/grid.hh", "dune/alugrid/dgf.hh"]
    gridModule = module(includes, typeName) # , dynamicAttr=True)
    return gridModule.LeafGrid(gridModule.reader(constructor))
def aluSimplexGrid(constructor, dimgrid=2, dimworld=2):
    from dune.grid.grid_generator import module, getDimgrid
    typeName = "Dune::Vem::Grid<"+str(dimgrid)+","+str(dimworld)+">"
    includes = ["dune/vem/misc/grid.hh"]
    gridModule = module(includes, typeName) # , dynamicAttr=True)
    return gridModule.LeafGrid(gridModule.reader(constructor))
def aluCubeGrid(constructor, dimgrid=2, dimworld=2):
    from dune.grid.grid_generator import module, getDimgrid
    typeName = "Dune::Vem::CubeGrid<"+str(dimgrid)+","+str(dimworld)+">"
    includes = ["dune/vem/misc/grid.hh"]
    gridModule = module(includes, typeName) # , dynamicAttr=True)
    return gridModule.LeafGrid(gridModule.reader(constructor))
def yaspGrid(constructor, dimgrid=None, coordinates="equidistant", ctype="double"):
    from dune.generator import Constructor
    from dune.grid.grid_generator import module, getDimgrid
    from dune.typeregistry import generateTypeName

    if not dimgrid:
        dimgrid = getDimgrid(constructor)
    if coordinates == "equidistant":
        coordinates = "Dune::EquidistantOffsetCoordinates"
    elif coordinates == "tensorproduct":
        coordinates = "Dune::TensorProductCoordinates"

    if not dimgrid:
        dimgrid = getDimgrid(constructor)
    coordinates, _ = generateTypeName(coordinates, ctype, dimgrid)
    typeName, includes = generateTypeName("Dune::Vem::YGrid", dimgrid, coordinates)
    includes += ["dune/vem/misc/grid.hh", "dune/grid/io/file/dgfparser/dgfyasp.hh"]

    ctor = Constructor([
              'Dune::FieldVector<'+ctype+', '+str(dimgrid)+'> lowerleft',
              'Dune::FieldVector<'+ctype+', '+str(dimgrid)+'> upperright',
              'std::array<int, '+str(dimgrid)+'> elements',
              'std::array<bool, '+str(dimgrid)+'> periodic',
              'int overlap'],
              ['std::bitset<'+str(dimgrid)+'> periodic_;',
               'for (int i=0;i<'+str(dimgrid)+';++i) periodic_.set(i,periodic[i]);',
               'return new DuneType(lowerleft,upperright,elements,periodic_,overlap);'],
              ['"lowerleft"_a', '"upperright"_a', '"elements"_a', '"periodic"_a', '"overlap"_a'])

    gridModule = module(includes, typeName, ctor) # , dynamicAttr=True)

    try:
        lowerleft  = constructor.lower
        upperright = constructor.upper
        elements   = constructor.division
        periodic   = constructor.param.get("periodic", [False,]*dimgrid)
        overlap    = constructor.param.get("overlap", 0)
        return gridModule.HierarchicalGrid(lowerleft,upperright,elements,periodic,overlap).leafView
    except AttributeError:
        return gridModule.reader(constructor).leafView

#################################################################
class TrivialAgglomerate:
    def __init__(self,grid,cubes=None):
        if cubes is None:
            from dune.geometry import quadrilateral, triangle
            try:
                if grid.type == quadrilateral:
                    cubes = True
                elif grid.type == triangle:
                    cubes = False
            except AttributeError:
                cubes = False
                assert False, "Unsupported grid element type for vem space"

        if cubes:
            self.minEdgeNumber = 4
        else:
            self.minEdgeNumber = 3
        self.size = grid.size(0)
    def __call__(self, idx):
        return idx
def trivialAgglomerate(constructor, cubes=False, globalRefine=None, **kwargs):
    if cubes:
        grid = aluCubeGrid(constructor, **kwargs)
    else:
        grid = aluSimplexGrid(constructor, **kwargs)
        if globalRefine is not None:
            grid.hierarchicalGrid.globalRefine(globalRefine)
    agglomerate = TrivialAgglomerate(grid, cubes)
    grid.hierarchicalGrid.agglomerate = agglomerate
    return grid

# http://zderadicka.eu/voronoi-diagrams/
from dune.vem.earcut import EarCut
#from scipy.spatial import Voronoi, voronoi_plot_2d, cKDTree
from scipy.spatial import Delaunay
import numpy

def crossProduct(A):
    x1 = (A[1][0] - A[0][0])
    y1 = (A[1][1] - A[0][1])
    x2 = (A[2][0] - A[0][0])
    y2 = (A[2][1] - A[0][1])
    return (x1*y2 - y1*x2)
def checkConvex(points):
    N = len(points)
    prev = 0
    curr = 0
    for i in range(N):
        temp = [points[i], points[(i + 1) % N], points[(i + 2) % N]]
        curr = crossProduct(temp)
        if (curr != 0):
            if (curr * prev < 0):
                return False
            else:
                prev = curr
    return True

try:
    import triangle
except ImportError:
    triangle = None

from sortedcontainers import SortedDict
import matplotlib.pyplot as plt
class PolyAgglomerate:
    def __init__(self,grid,index):
        indexSet = grid.indexSet
        self.polys = numpy.zeros(grid.size(0),int)
        self.size = 0
        for e in grid.elements:
            idx = index[PolyAgglomerate.roundBary(e.geometry.center)]
            self.polys[indexSet.index(e)] = idx
            self.size = max(self.size,idx+1)

    def __call__(self,idx):
        return self.polys[idx]

    @staticmethod
    def roundBary(a):
        return tuple(round(aa,8) for aa in a)
    @staticmethod
    def construct(cubes,convex,vertices,polygons):
        index = SortedDict()
        if cubes:
            for i,poly in enumerate(polygons):
                assert len(poly)==4
                bary = [sum([vertices[p][i] for p in poly]) / 4 for i in range(2)]
                index[PolyAgglomerate.roundBary(bary)] = i
                polygons[i][2], polygons[i][3] = poly[3], poly[2]
            domain = {"vertices": vertices.astype(float), "cubes": polygons.astype(int)}
        else:
            vertices = numpy.array(vertices)
            tr = []
            earCut = EarCut()
            for nr, p in enumerate(polygons):
                N = len(p)
                if not convex:
                    tri = earCut(vertices,p)
                elif False: # not convex and not checkConvex(vertices[p]):
                    if not triangle:
                        raise ValueError("""
a grid with non convex polygons requires the 'triangle' package.
Run 'pip install triangle' and try again.
Note that 'convex=False' is the default - if all your polygons are convex
change the parameter to 'True' which will also speedup the grid construction.
""")
                    # use triangle
                    e = [ [p[i],p[(i+1)%N]] for i in range(N) ]
                    domain = { "vertices":vertices, "segments":numpy.array(e) }
                    B = triangle.triangulate(domain,opts="p")
                    tri = B["triangles"]
                    # triangle.compare(plt, domain, B)
                    # plt.show()
                else: # use scipy
                    p = numpy.array(p)
                    poly = numpy.append(p,[p[0]])
                    vert = vertices[p, :]
                    tri = p[Delaunay(vert).simplices]
                tr += [{"triangles":tri}]
                bary = [ (vertices[p0]+vertices[p1]+vertices[p2])/3.
                         for p0,p1,p2 in tr[-1]["triangles"] ]
                for b in bary:
                    index[PolyAgglomerate.roundBary(b)] = nr
            domain = {"vertices":  numpy.array(vertices).astype(numpy.float64),
                      "simplices": numpy.vstack([ t["triangles"] for t in tr ]).astype(int)}
        return domain, index
def polyAgglomerate(constructor,cubes=False,convex=None):
    if convex is None:
        convex = constructor.get("convex",False)
    suffix = "poly"+str(len(constructor["polygons"]))
    domain, index = PolyAgglomerate.construct(cubes,convex,
                                                constructor["vertices"],
                                                constructor["polygons"])
    if cubes:
        grid = aluCubeGrid(domain)
    else:
        grid = aluSimplexGrid(domain)
    agglomerate = PolyAgglomerate(grid,index)
    agglomerate.minEdgeNumber = min([len(p) for p in constructor["polygons"]])
    grid.hierarchicalGrid.agglomerate = agglomerate
    return grid

def polyGrid(constructor,cubes=False, convex=None,**kwargs):
    from dune.alugrid import ALUGridEnvVar
    verbosity = ALUGridEnvVar('ALUGRID_VERBOSITY_LEVEL', 0)
    if isinstance(constructor,dict) and constructor.get("polygons",None) is not None:
        grid = polyAgglomerate(constructor,cubes,convex)
    else:
        grid = trivialAgglomerate(constructor, cubes, **kwargs)
    # in case of a carteisan domain store if old or new boundary ids was used
    # this can be removed in later version - it is only used in dune-fem
    # to give a warning that the boundary ids for the cartesian domains have changed
    try:
        grid.hierarchicalGrid._cartesianConstructionWithIds = constructor.boundaryWasSet
    except AttributeError:
        pass
    return grid

import weakref
agglomerationStorage_ = weakref.WeakKeyDictionary()
def removeAgglo_(agglo):
    for key, value in agglomerationStorage_.items():
        if value == agglo:
            del agglomerationStorage_[key]
            break
def retrieveAgglo_(gv):
    return agglomerationStorage_.get(gv,None)
def insertAgglo_(gv, agglo):
    agglomerationStorage_[gv] = agglo


def plotPolygons(domain):
    figure = plt.figure()
    axe = figure.add_subplot(111)
    for cell in domain["polygons"]:
        polygon = plt.Polygon(
            [ domain["vertices"][i] for i in cell ],
            edgecolor="black",
            facecolor="white"
        )
        axe.add_patch(polygon)
    axe.set_aspect('equal')
    axe.autoscale()
    return figure

try:
    import meshio
    def writePolygons(fileBase, domain, fileFormat="vtu"):
        points = list( domain["vertices"] )
        polys = list( domain["polygons"] )

        # in vtk points are 3d
        points = np.insert(points, 2, 0, axis=1)

        # sort polygons into buckets accoring to equal sizes
        polys.sort(key=len)
        cells = [[polys[0]]]
        for p in polys[1:]:
            if len(p) > len(cells[-1][0]):
                cells += [[p]]
            else:
                cells[-1] += [p]
        cells = [("polygon", c) for c in cells]
        meshio.write_points_cells(f"{fileBase}.{fileFormat}", points,
                                  cells, file_format=fileFormat)
except ImportError:
    def writePolygons(fileBase, domain, fileFormat="vtu"):
        raise ImportError("dune.vem.writePolygons requires the meshio package")
