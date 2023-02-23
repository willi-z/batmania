# Data
Diff = 1e-14  # solid diffusivity [m^2/s]
r_0 = 10e-6  # particle radius [m]

c_max = 12000  # maximum Li concentration [mol/m^3]
c_0 = 9600  # initial Li concentration [mol/m^3]

j_0 = 5000 * r_0 / 3 / 1800  # Li flux [mol/m^2/s]

dt = 1  # time steps [s]
t_discharge = 0.5 * 60 * 60  # simulation time [s]
t_rest = 1.0 * 60 * 60  # simulation time [s]
t_charge = 0.5 * 60 * 60  # simulation time [s]

t_end = t_discharge + t_rest + t_charge + t_rest
t_steps = round(t_end / dt + 1)


def f_j(t):
    if t <= t_discharge:
        return j_0
    else:
        if t - t_discharge <= t_rest:
            return 0
        else:
            if t - t_discharge - t_rest <= t_charge:
                return -j_0
            else:
                return 0
