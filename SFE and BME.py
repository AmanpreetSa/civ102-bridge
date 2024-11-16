import numpy as np
import matplotlib.pyplot as plt
import math
# Beam properties
L = 1200  # Length of the beam in mm
n = 1200  # divide in 1 mm
P = 400   # force (N)
x = np.linspace(0, L, 1201)   #.linspace to approximate the beam length
x_train = [-856, -680, -516, -340, -176, 0] # distance/length between point loads
point_loads = [400/6, 400/6, 400/6, 400/6, 400/6, 400/6]
n_train = 3 # number of train locations
dx = 1
# Reactions at supports for a simply supported beam under uniform load
Ra = 0
Rb = 0
dx = 1
#FDi = np.zeros(n_train, n)
#BMDi = np.zeros(n_train, n)
SFE = [[] for i in range(2057)]
BME = [[] for i in range(2057)]
for xj in range(2057): # beginning at the first wheel on the bridge and stop at the last train leaving the bridge
    train_location = [0, 0, 0, 0, 0, 0] #reset train's location when it moves forward 1mm
    moment_A = 0
    Fyb = 0
    Fya = 0
    total_load = 0
    #reset all the number to 0 when the train has moved
    for i in range(len(x_train)):
        train_location[i] = x_train[i] + xj #set the location of the train
        if 0 <= train_location[i] <= 1200: #detect whether the wheel is on the bridge or not
            moment_A += point_loads[i] * train_location[i] # calculate the moment
            total_load += point_loads[i] #calculate the total load
    Fyb = moment_A / L #calculate the reaction force at the end of the bridge
    Fya = total_load - Fyb #calculate the reaction force at the beginning of the bridge
    cur_SFD = np.full(n + 1, Fya) #initial set of SFD
    #create cur_SFD at one single location of the train
    for i in range(len(x_train)):
        if 0 <= train_location[i] <= 1200:
            indices = np.where(x >= train_location[i])
            cur_SFD[indices] -= point_loads[i]
    #calculate BMD
    cur_BMD = np.cumsum(cur_SFD) * dx
    # put all SFD and BMD into SFE and BME
    SFE[xj].append(cur_SFD.tolist())
    BME[xj].append(cur_BMD.tolist())
#initial sets for maximum SFD and BMD
max_SFD = SFE[0][0]
max_BMD = BME[0][0]
# find maximum SFD and BMD
for i in range(1201):
    for xj in range(2057):
        if abs(max_SFD[i]) <= abs(SFE[xj][0][i]):
            max_SFD[i] = SFE[xj][0][i]
            max_SFD_xj = xj
        if abs(max_BMD[i]) <= abs(BME[xj][0][i]):
            max_BMD[i] = BME[xj][0][i]
            max_BMD_xj = xj


# for i in range(n_train):
#
#     train_location = [0, 0, 0, 0, 0, 0]
#     moment_A = 0
#     Fyb = 0
#     Fya = 0
#     for j in range(len(x_train)):
#         train_location[j] = x_train[j] + n_train * 120  #distance each wheel away from the beginning of the bridge
#         moment_A += (P/6) * train_location[j]
#         Fyb = moment_A / 1200
#         Fya = P - Fyb
#         SFD = np.full(n, Fya)   #initial set of SFD
#         for xj in train_location:
#             indices = np.where(x >= xj)
#             SFD[indices] -= P/6     # find y value for the SFD
#         # BMD Calculation
#         BMD = np.cumsum(SFD) * dx



# plotting SMD
plt.figure(figsize=(15, 5))
plt.plot(x, max_SFD, label='Shear Force V(x)', color='blue')
plt.title('Shear Force Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Shear Force (kN)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

# plotting BMD
plt.figure(figsize=(12, 6))
plt.plot(x, max_BMD, label='Bending Moment M(x)', color='red')
plt.title('Bending Moment Diagram')
plt.xlabel('Position along the beam (m)')
plt.ylabel('Bending Moment (kN·m)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()