from scipy.optimize import newton
from data import f_U_ocp_ext

y_initial = newton(lambda y: 3.5102 - f_U_ocp_ext(y), 1.0, tol=1e6)
print(y_initial)
print(f_U_ocp_ext(y_initial))
print(1 - y_initial)
print(22e-4)

dy = newton(lambda dy: f_U_ocp_ext(1.0 - 1e-4, dy) - 3.5102, 22e-4)
print(dy)
print(f_U_ocp_ext(1.0, dy))
