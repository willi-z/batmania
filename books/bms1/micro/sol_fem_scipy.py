from scipy.integrate import solve_ivp
import numpy as np
import polars as pl
from pathlib import Path
from fem import Mass, Fick, bc, u0, dofs, x_locs
from data import f_j, t_end, t_steps

# import plotly.express as px


Mass_inv = np.linalg.pinv(Mass.toarray())


def py_plett(t, u):
    j = f_j(t)
    return np.matmul(Mass_inv, (-j * bc - Fick.dot(u)))


tspan = [0.0, t_end]

# print(np.shape(py_particle(0, u0)))
sol = solve_ivp(
    py_plett,
    tspan,
    u0,
    # method="Radau",
    dense_output=True,
)

t = np.linspace(0, t_end, t_steps)
c_solid = sol.sol(t).T
cs = np.zeros(len(t))
js = np.zeros(len(t))
locs = [None] * len(t)

for i in range(len(t)):
    surf_t = c_solid[i]
    cs[i] = surf_t[dofs]
    js[i] = f_j(t[i])
    locs[i] = x_locs


df = pl.DataFrame(
    {
        "t": t,  # time
        "j": js,  # ion flux
        "cs": cs,  # surface concentration
        "ct": c_solid,
        "x_locs": locs,
    }
)
print(df)

storageFile = Path.cwd() / "books" / "bms1" / "micro" / "results" / "sol_fem_scipy.json"
print(storageFile.absolute())
df.write_json(storageFile)
