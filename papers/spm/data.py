import numpy as np

# Data
Diff = 2.2e-9  # [cm^2 s^-1] 1e-9#
β = 0.5  # [ ]

r_0 = 5e-4  # [cm]

c_l = 1.0  # [mol dm^-3]
c_0 = 23.7  # [mol dm^-3]
c_t = 23.7  # [mol dm^-3]
c_theta = 0  # [mol dm^-3] (intial value)
k = 0.00019  # [cm^(5/2) s^-1 mol^(-1/2)]
nu = 1  # [mV s^-1]
a = 1.36  # []

U_max = 4.3102  # [V]

# convertion
Diff *= 1e-4  # [m^2 s^-1]
r_0 *= 1e-2  # [m]
c_l *= 1e3  # [mol m^-3]
c_0 *= 1e3  # [mol m^-3]
c_t *= 1e3  # [mol m^-3]
c_theta *= 1e3  # [mol m^-3]
k *= np.power(1e-2, (5 / 2))  # [m^(5/2) s^-1 mol^(-1/2)]
nu *= 1e-3  # [V s^-1]

ac = k * r_0 * np.power(c_l, β) / Diff

const = dict(
    R=8.314472,  # [m^2 kg s^-2 K^-1 mol^-1]
    F=96485.3415,  # [m^2 kg s^-2 K^-1 mol^-1]
    T=25 + 273.15,  # [K]
)

y_s_max = 0.998432

cs = c_0 * (1 - 1e-4)  # * (1-4001e-6)
print(f"y_s: {cs/c_0}")


def f_U_ocp(y_s):
    """
    The open-circuit potential as a function of the dimensionaless
    concentration of lithium-ions at the surface of the manganese dioxide particle
    """
    return (
        4.19829
        + 0.0565661 * np.tanh(-14.5546 * y_s + 8.60942)
        - 0.0275479 * (np.power(abs(y_s_max - y_s), -0.492465) - 1.90111)
        - 0.157123 * np.exp(-0.04738 * np.power(y_s, 8))
        + 0.810239 * np.exp(-40.0 * y_s + 5.355)
    )


def f_U_ocp_ext(y_s):
    dy = 22e-4

    if y_s >= y_s_max - dy:
        c = y_s_max - dy
        h = 1e-6
        U_ocp_max = f_U_ocp(y_s_max - dy)
        U_ocp_max_h = f_U_ocp(y_s_max - dy - h)
        return U_ocp_max + (U_ocp_max - U_ocp_max_h) / (h) * (y_s - c)
    return f_U_ocp(y_s)


def f_U_ocp_alt(y):
    return 4.2 - 0.25 * y


# plot!(y_s, U_ocp(y_s), ylims=(3,4.5))


def f_tau(t):
    return t * Diff / (r_0**2)


def f_t(tau):
    return tau * r_0**2 / Diff


def f_jc_η(c_s, η):
    # if y_s >= 1.0:
    #     print(f"y_s: {y_s}")
    # if η < 0.0:
    #     print(f"η: {η}")

    j0 = k * np.power(c_l, 1 - β) * np.power(c_t - c_s, 1 - β) * np.power(c_s, β)

    j = j0 * (
        np.exp(((1 - β) * const["F"] * η) / (const["R"] * const["T"]))
        - np.exp(-1 * (β * const["F"] * η) / (const["R"] * const["T"]))
    )

    return j


def f_jc(c_s, U_app):
    # U = f_U_ocp(y_s)
    # U = f_U_ocp_alt(y_s)
    U_opc = f_U_ocp_ext(c_s / c_0)
    η = U_app - U_opc
    return f_jc_η(c_s, η)


def f_jy_η(y_s, η):
    # if y_s >= 1.0:
    #     print(f"y_s: {y_s}")
    # if η < 0.0:
    #     print(f"η: {η}")

    j0 = a * np.power(y_s, β) * np.power(1 - y_s, 1 - β)

    j = j0 * (
        np.exp(((1 - β) * const["F"] * η) / (const["R"] * const["T"]))
        - np.exp(-1 * (β * const["F"] * η) / (const["R"] * const["T"]))
    )

    return j


def f_jy(y_s, U_app):
    # U = f_U_ocp(y_s)
    # U = f_U_ocp_alt(y_s)
    U_opc = f_U_ocp_ext(y_s)
    η = U_app - U_opc
    return f_jy_η(y_s, η)


U_start = f_U_ocp_ext(cs / c_0)  # f_U_ocp_ext(1.0-1e-4) + 7e-1# 3.5102    # [V]
# U_ocp_ext = f_U_ocp_ext(1.0) # y_s_max-2e-3
print(f"U_0: {U_start}")
dU = U_max - U_start
t_charge = dU / nu
t_hold = dU / nu * 0.0

dt = 1  # [s]
t_end = 2 * t_charge + t_hold
t_steps = round(t_end / dt) + 1


def f_U_app_t(t):
    if t <= t_charge:
        return U_start + t * nu
    elif t - t_charge <= t_hold:
        return U_max
    else:
        return U_max - (t - t_charge - t_hold) * nu


def f_U_app_tau(tau):
    return f_U_app_t(f_t(tau))
