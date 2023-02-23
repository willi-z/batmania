import plotly.graph_objects as go
from data import f_U_app_t, t_end, t_steps
import numpy as np


ts = np.linspace(0, t_end, t_steps)
Uapp = np.zeros(len(ts))
for i in range(len(ts)):
    Uapp[i] = f_U_app_t(ts[i])

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=ts, y=Uapp, mode="lines", name="U_app"))

# fig.show()
fig.write_image("U_app.png")
