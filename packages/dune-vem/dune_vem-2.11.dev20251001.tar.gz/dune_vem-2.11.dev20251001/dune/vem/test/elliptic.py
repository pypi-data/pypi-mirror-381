from ufl import *
import dune.ufl

parameters = {"newton.linear.tolerance": 1e-12,
              "newton.linear.preconditioning.method": "jacobi",
              "penalty": 40,  # for the dg schemes
              "newton.linear.verbose": False,
              "newton.verbose": False
              }

def elliptic(space, exact):
    # set up scheme, df, and solve
    u = TrialFunction(space)
    v = TestFunction(space)
    x = SpatialCoordinate(space)

    massCoeff = 1+sin(dot(x,x))       # factor for mass term
    diffCoeff = 1-0.9*cos(dot(x,x))

    a = (diffCoeff*inner(grad(u),grad(v)) + massCoeff*dot(u,v) ) * dx

    # finally the right hand side and the boundary conditions
    b = (-div(diffCoeff*grad(exact[0])) + massCoeff*exact[0] ) * v[0] * dx
    dbc = [dune.ufl.DirichletBC(space, exact, i+1) for i in range(4)]

    df = space.interpolate([0],name="solution")
    scheme = dune.vem.vemScheme( [a==b, *dbc], space, solver="cg",
                            gradStabilization=diffCoeff,
                            massStabilization=massCoeff,
                            parameters=parameters )

    info = scheme.solve(target=df)

    edf = exact-df
    err = [inner(edf,edf), inner(grad(edf),grad(edf))]

    return err