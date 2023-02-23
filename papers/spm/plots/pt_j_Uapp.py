from pathlib import Path
import polars as pl
import numpy as np
import plotly.graph_objects as go
from spm.data import U_start, U_max

storageFile = Path.cwd() / "paper_spm" / "results" / "sol_stiff.json"
print(storageFile)
df = pl.read_json(storageFile)
print(df)

U_app = df.get_column("U_app").view()
j = df.get_column("j").view()

fig = go.Figure()
fig.add_trace(go.Scatter(x=U_app, y=j, mode="lines", name="U_app"))
fig.update_layout(
    xaxis_title="U_app [V]",
    yaxis_title="j [ ]",
    template="none",
    autosize=False,
    width=500,
    height=400,
    margin=dict(l=40, r=10, t=10, b=40, pad=3),
)


x_min = np.floor(U_start * 10) / 10
x_max = np.ceil(U_max * 10) / 10
print(f"{x_min} | {U_start}")
print(f"{x_max} | {U_max}")
dx = x_max - x_min

# https://plotly.com/python/axes/
fig.update_xaxes(
    ticklabelstep=2,
    nticks=int(dx * 40),
    range=[x_min - dx * 0.02, x_max + dx * 0.02],
    showline=True,
    linewidth=2,
    linecolor="black",
    mirror=True,
    gridcolor="black",
    griddash="dot",
)

y_min = -0.4
y_max = 0.4
dy = y_max - y_min

fig.update_yaxes(
    range=[y_min - dy * 0.02, y_max + dy * 0.02],
    showline=True,
    linewidth=2,
    linecolor="black",
    mirror=True,
    gridcolor="black",
    griddash="dot",
    zeroline=False,
)

# fig.show()
fig.write_image("pt_j_Uapp.png", scale=2)  # width=600, height=350,
