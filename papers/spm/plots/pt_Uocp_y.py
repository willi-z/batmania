import numpy as np
from pathlib import Path
import plotly.graph_objects as go
from papers.spm.data import f_U_ocp, f_U_ocp_ext, y_s_max

x_min = 0.18
x_max = 1.0
x_break = y_s_max - 0.006360215613507735
y_old = np.linspace(x_min, x_break, 1000)
Uocp_old = np.zeros(len(y_old))
for i in range(len(y_old)):
    Uocp_old[i] = f_U_ocp(y_old[i])

y_ext = np.linspace(x_break, x_max, 10)
Uocp_ext = np.zeros(len(y_ext))
for i in range(len(y_ext)):
    Uocp_ext[i] = f_U_ocp_ext(y_ext[i])

fig = go.Figure()
fig.add_trace(go.Scatter(x=y_old, y=Uocp_old, mode="lines", name=r"$U_{ocp}$"))
fig.add_trace(
    go.Scatter(
        x=y_ext,
        y=Uocp_ext,
        # mode='lines',
        mode="lines",
        name=r"$U_{ext}$",
    )
)

fig.update_layout(
    xaxis_title=r"$y \left[ \; \right]$",
    yaxis_title=r"$U_{ocp} \left[ \; \right]$",
    template="none",
    autosize=False,
    width=500,
    height=300,
    margin=dict(l=50, r=80, t=5, b=40, pad=3),
)


dx = x_max - x_min

# https://plotly.com/python/axes/
fig.update_xaxes(
    ticklabelstep=1,
    nticks=int(dx * 20),
    range=[0.1, 1.1],
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
imageFile = Path.cwd() / "papers" / "spm" / "results" / "pt_Uocp_y.png"
fig.write_image(imageFile, scale=2)  # width=600, height=350,
