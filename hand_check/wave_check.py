"""Hand check for the epoxy block impact (1D wave estimates)."""
import math
E, nu, rho = 3e9, 0.35, 1200.0      # epoxy
L = 0.200                           # block height, m
K = E / (3 * (1 - 2 * nu)); G = E / (2 * (1 + nu))
c_bar = math.sqrt(E / rho)                  # thin bar
c_p = math.sqrt((K + 4 * G / 3) / rho)      # constrained (compression) wave
c_s = math.sqrt(G / rho)                    # shear wave
print(f"c_bar = {c_bar:.0f} m/s, c_p = {c_p:.0f} m/s, c_s = {c_s:.0f} m/s")

# 0 deg: 1.414 m/s along the height. Top travels v*L/c before the reflected wave stops it.
v = math.hypot(1, 1)
print(f"0 deg : u = v L / c_p  = {v * L / c_p * 1e3:.3f} mm (bar: {v * L / c_bar * 1e3:.3f} mm)")
print(f"        sigma = rho c v = {rho * c_p * v / 1e6:.2f} MPa")

# 45 deg: 1 m/s along the height (compression) + 1 m/s sideways (shear)
u_n = 1.0 * L / c_p; u_s = 1.0 * L / c_s
print(f"45 deg: u = sqrt({u_n*1e3:.3f}^2 + {u_s*1e3:.3f}^2) = {math.hypot(u_n, u_s) * 1e3:.3f} mm")
