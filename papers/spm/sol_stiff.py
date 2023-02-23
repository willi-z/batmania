from scipy.integrate import solve_ivp
import numpy as np
import polars as pl
from fem import Mass, Fick, bc, u0, get_cs, dofs, x_locs
from data import f_jc, c_0, f_U_app_t, t_end, Diff, r_0
from pathlib import Path

# import plotly.express as px


Mass_inv = np.linalg.pinv(Mass.toarray())


def py_particle(t, u):
    U_app = f_U_app_t(t)
    j = f_jc(get_cs(u), U_app)  # / r_0
    return np.matmul(Mass_inv, (-j * bc - Fick.dot(u)))


tspan = [0.0, t_end]
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html
sol = solve_ivp(
    py_particle,
    tspan,
    u0,
    method="Radau",  # Radau, BDF, LSODA
    # atol=1e-6,
    dense_output=True,
)


t = np.linspace(0, t_end, 2000)

c_solid = sol.sol(t).T

print(np.shape(t))
print(np.shape(c_solid))

U_app = np.zeros(len(t))
ys = np.zeros(len(t))
js = np.zeros(len(t))
locs = [None] * len(t)
for i in range(len(t)):
    U_app[i] = f_U_app_t(t[i])
    surf_t = c_solid[i]
    ys[i] = surf_t[dofs]  # surf_t[0][i]
    js[i] = f_jc(ys[i], U_app[i])
    locs[i] = x_locs


df = pl.DataFrame(
    {
        "t": t,  # time
        "U_app": U_app,  # applied voltage
        "j": js * (r_0 / (Diff * c_0)),  # unitless ion flux
        "cs": ys,  # surface concentration
        "ct": c_solid,
        "x_locs": locs,
    }
)
print(df)

storageFile = Path.cwd() / "paper" / "spm" / "results" / "sol_stiff.json"
print(storageFile.absolute())
df.write_json(storageFile)
