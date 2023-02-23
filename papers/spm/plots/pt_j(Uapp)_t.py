from pathlib import Path
import polars as pl
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from papers.spm.data import t_charge, t_hold, f_U_ocp_ext, c_0

storageFile = Path.cwd() / "papers" / "spm" / "results" / "sol_stiff.json"
print(storageFile)
df = pl.read_json(storageFile)

ts = df.get_column("t").view()
Uapp = df.get_column("U_app").view()
cs = df.get_column("cs").view()
j = df.get_column("j").view()

Uocp = np.zeros(len(cs))
for i in range(len(cs)):
    Uocp[i] = f_U_ocp_ext(cs[i] / c_0)

p_charge = 0.8
x_min = p_charge * t_charge
x_max = x_min + t_hold + 2 * (1 - p_charge) * t_charge

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(
        x=ts,
        y=Uapp,
        mode="lines",
        name="Uapp(t)",
    ),
    secondary_y=True,
)
fig.add_trace(
    go.Scatter(
        x=ts,
        y=Uocp,
        mode="lines",
        name="Uocp(t)",
    ),
    secondary_y=True,
)
fig.add_trace(
    go.Scatter(x=ts, y=j, mode="lines", name="j(t)"),
    secondary_y=False,
)


fig.update_layout(
    template="none",
    autosize=False,
    width=500,
    height=400,
    margin=dict(l=40, r=5, t=10, b=40, pad=1),
)


dx = x_max - x_min

# https://plotly.com/python/axes/
fig.update_xaxes(
    title_text="t [s]",
    ticklabelstep=1,
    nticks=10,
    range=[x_min - dx * 0.02, x_max + dx * 0.02],
    showline=True,
    linewidth=2,
    linecolor="black",
    mirror=True,
    # gridcolor='black', griddash='dot',
)

y_min = -0.4
y_max = 0.4
dy = y_max - y_min

fig.update_yaxes(
    secondary_y=False,
    title_text="j [ ]",
    range=[y_min, y_max],
    showline=True,
    linewidth=2,
    linecolor="black",  # mirror=True,
    # gridcolor='black', griddash='dot',
    zeroline=False,
)

fig.update_yaxes(
    secondary_y=True,
    title_text="U [V]",
    range=[4, 4.4],
    showline=True,
    linewidth=2,
    linecolor="black",
    # gridcolor='black', griddash='dot',
    zeroline=False,
)

# fig.show()
imageFile = Path.cwd() / "papers" / "spm" / "results" / "pt_j(Uapp)_t.png"
fig.write_image(imageFile, scale=2)  # width=600, height=350,
