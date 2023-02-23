import numpy as np
from pathlib import Path
import plotly.graph_objects as go
from papers.spm.data import f_jy_η

x_min = 0.8
x_max = 1.0
y = np.linspace(x_min, x_max, 100)
etas = [0.1, 0.15, 0.2]

fig = go.Figure()
for eta in etas:
    j = f_jy_η(y, eta)
    fig.add_trace(go.Scatter(x=y, y=j, mode="lines", name=f"j(η={eta})"))

fig.update_layout(
    xaxis_title="y [ ]",
    yaxis_title="j [ ]",
    template="none",
    autosize=False,
    width=500,
    height=400,
    margin=dict(l=40, r=0, t=10, b=40, pad=3),
)


dx = x_max - x_min

# https://plotly.com/python/axes/
fig.update_xaxes(
    ticklabelstep=1,
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
    # range=[y_min - dy * 0.02, y_max + dy * 0.02],
    showline=True,
    linewidth=2,
    linecolor="black",
    mirror=True,
    gridcolor="black",
    griddash="dot",
    zeroline=False,
)

# fig.show()
imageFile = Path.cwd() / "papers" / "spm" / "results" / "pt_j(eta)_y.png"
fig.write_image(imageFile, scale=2)  # width=600, height=350,
