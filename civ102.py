import numpy as np
import matplotlib.pyplot as plt

# Beam properties
L = 1200  # Length of the beam in mm
n = 1200  # divide in 1 mm
P = 400   # force (N)
x = np.linspace(0, L, 1200)   #.linspace to approximate the beam length
x_train = [52, 228, 392, 568, 732, 908] # distance/length between point loads
point_loads = [400/6, 400/6, 400/6, 400/6, 400/6, 400/6]
n_train = 3 # number of train locations
dx = 1
# Reactions at supports for a simply supported beam under uniform load
Ra = 0
Rb = 0

#FDi = np.zeros(n_train, n)
#BMDi = np.zeros(n_train, n)

for i in range(n_train):
    train_location = [0, 0, 0, 0, 0, 0]
    moment_A = 0
    Fyb = 0
    Fya = 0
    for j in range(len(x_train)):
        train_location[j] = x_train[j] + n_train * 120  #distance each wheel away from the beginning of the bridge
        moment_A += (P/6) * train_location[j]
        Fyb = moment_A / 1200
        Fya = P - Fyb
        SFD = np.full(n, Fya)   #initial set of SFD
        for xj in train_location:
            indices = np.where(x >= xj)
            SFD[indices] -= P/6     # find y value for the SFD
        # BMD Calculation
        BMD = np.cumsum(SFD) * dx



'''
# plotting SMD
plt.figure(figsize=(15, 5))
plt.plot(x, calc_shear_force, label='Shear Force V(x)', color='blue')
plt.title('Shear Force Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Shear Force (kN)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

# plotting BMD
plt.figure(figsize=(12, 6))
plt.plot(x, calc_bending_moment, label='Bending Moment M(x)', color='red')
plt.title('Bending Moment Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Bending Moment (kN·m)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
'''
