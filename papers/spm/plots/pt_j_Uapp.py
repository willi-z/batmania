from pathlib import Path
import polars as pl
import numpy as np
import plotly.graph_objects as go
from papers.spm.data import U_start, U_max

storageFile = Path.cwd() / "papers" / "spm" / "results" / "sol_stiff.json"
print(storageFile)
df = pl.read_json(storageFile)
print(df)

U_app = df.get_column("U_app").view()
j = df.get_column("j").view()

fig = go.Figure()
fig.add_trace(go.Scatter(x=U_app, y=j, mode="lines", name=r"$U_{app}$"))
fig.update_layout(
    xaxis_title=r"$U_{app} \left[ V \right]$",
    yaxis_title=r"$j \left[ \; \right]$",
    template="none",
    autosize=False,
    width=500,
    height=400,
    margin=dict(l=40, r=10, t=5, b=40, pad=3),
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
imageFile = Path.cwd() / "papers" / "spm" / "results" / "pt_j_Uapp.png"
fig.write_image(imageFile, scale=2)  # width=600, height=350,
