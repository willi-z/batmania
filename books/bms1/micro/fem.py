from skfem import MeshLine, Basis, ElementLineP2, BilinearForm, LinearForm
from skfem.helpers import dot, grad
import numpy as np
from data import r_0, Diff, c_0

# from data.book_plett import r_0, Diff, c_0

# SIMULATION CONTROL
n_points_particle = 20 + 1
# MESHING
space = np.linspace(0, 1, n_points_particle)
mesh = MeshLine(space).with_boundaries(
    {"inner": lambda xi: xi[0] == 0, "surface": lambda xi: xi[0] == 1.0}
)

basis = Basis(mesh, ElementLineP2())  # ElementLineHermite
basis_surf = basis.boundary("surface")
dofs = basis.get_dofs("surface")


@BilinearForm
def M(conc, v, w):
    r = w.x[0]
    return r**2 * r_0 * conc * v


@BilinearForm
def A(conc, v, w):
    r = w.x[0]
    return Diff * r**2 / r_0 * dot(grad(conc), grad(v))


@LinearForm
def b(v, w):
    return dot(w.n, v)  # * r_0


Mass = M.assemble(basis)
Fick = A.assemble(basis)
bc = b.assemble(basis_surf)


# INTIAL CONDITIONS
def inital(x):
    return np.ones((x.shape[1], x.shape[2])) * c_0


u0 = basis.project(inital)
# u0[dofs] = c_s


def get_cs(us):
    return us[dofs]


x_locs = basis.doflocs[0]
# print(f"u0: {u0}")
# print(f"u_surf: {u0[dofs][0]}")
# print(np.shape(u0))
# print(type(u0)) # np.ndarray
