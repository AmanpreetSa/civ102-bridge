# Import libraries to help with calculations and plotting
import numpy as np
import matplotlib.pyplot as plt
import math

#Calculate ybar
def calculate_ybar(shape_of_crosssection):
    sum_Ai_di = 0
    sum_Ai = 0
    for i in range(len(shape_of_crosssection)):
        # ybar = sum(Ai*di)/sum(Ai)
        sum_Ai_di += shape_of_crosssection[i][0] * shape_of_crosssection[i][1] * shape_of_crosssection[i][2]
        sum_Ai += shape_of_crosssection[i][0] * shape_of_crosssection[i][1]
    ybar = sum_Ai_di / sum_Ai
    return ybar

#Calculate I
def calculate_I(shape_of_cresssection, ybar):
    sum_I0 = 0
    sum_Ai_d2 = 0
    for i in range(len(shape_of_cresssection)):
        # I = sum(I0) + sum(Ai*(d)^2)
        sum_I0 += (shape_of_cresssection[i][0] * (shape_of_cresssection[i][1])**3) / 12
        d = shape_of_cresssection[i][2] - ybar
        sum_Ai_d2 += shape_of_cresssection[i][0] * shape_of_cresssection[i][1] * (d**2)
    I = sum_I0 + sum_Ai_d2
    return I

#Calculate for Q at certain height y
def calculate_Q(shape_of_crosssection, y, ybar):
    Q = 0
    for i in range(len(shape_of_crosssection)):
        b_i = shape_of_crosssection[i][0]
        h_i = shape_of_crosssection[i][1]
        y_i = shape_of_crosssection[i][2]  # centroid of the ith part from the bottom edge

        ytop_i = y_i + h_i / 2  # top edge of the ith part
        ybot_i = y_i - h_i / 2  # bottom edge of the ith part

        if y >= ytop_i:
            # entire part is below y
            A_i = b_i * h_i
            d_i = y_i - ybar
            Q += A_i * d_i
        elif y <= ybot_i:
            # entire part is above y; no contribution to Q
            continue
        else:
            # this part is partially below y
            h_partial = y - ybot_i
            A_i = b_i * h_partial
            centroid_i = ybot_i + h_partial / 2
            d_i = centroid_i - ybar
            Q += A_i * d_i

    return abs(Q)
            
#Calculate flextual stresses
def calculate_flextual_strss(max_BMD, ybar, height, I):
    # sigma = My/I
    if max_BMD > 0: # check the sign of the BMD
        tension_stress = max_BMD * ybar / I
        compression_stress = max_BMD * (height - ybar) / I
    else:
        compression_stress = max_BMD * ybar / I
        tension_stress= max_BMD * (height - ybar) / I
    return tension_stress, compression_stress

# Calculate shear stress
def calculate_tau(max_SFD, Q, I, b):
    # tau = VQ/Ib
    return (max_SFD * Q) / (I * b)

#Calculate flex_buck
def calculate_flex_buck(K, E, mu, t, b):
    # sigma_buck = (K*pi^2*E)/12*(1-mu^2)) * (t/b)^2
    return ((K * (math.pi**2) * E) / (12 * (1 - mu**2))) * ((t / b)**2)

#Calculate shear buck
def  calculate_shear_buck(E, mu, t, a, h):
    # tau_buck = (5*pi^2*E)/12*(1-mu^2)) * ((t/a)^2 + (t/h)^2)
    return ((5 * (math.pi**2) * E) / (12 * (1 - mu**2))) * ((t / a)**2 + (t / h)**2)

#Calculate FOS
def calculate_FOS(sigma_ten, sigma_bot, sigma_comp, sigma_top, sigma_buck1, sigma_buck2, sigma_buck3, tau_max, tau_cent, tau_glue_max, tau_glue, tau_buck):
    FOS = {}
    FOS['tension'] = sigma_ten / sigma_bot
    FOS['compression'] = sigma_comp / sigma_top
    FOS['flexbuck1'] = sigma_buck1 / sigma_top
    FOS['flexbuck2'] = sigma_buck2 / sigma_top
    FOS['flexbuck3'] = sigma_buck3 / sigma_top
    FOS['shear'] = tau_max / tau_cent
    FOS['glue'] = tau_glue_max / tau_glue
    FOS['shearbuck'] = tau_buck / tau_cent
    return FOS

#Visualizing; finding the shear force and bending moment capacities 
def visualize(FOS, max_BMD, max_SFD):
    M_fail_ten = [0] * 1201
    M_fail_comp = [0] * 1201
    M_fail_buck1 = [0] * 1201
    M_fail_buck2 = [0] * 1201
    M_fail_buck3 = [0] * 1201
    V_fail_shear = [0] * 1201
    V_fail_glue = [0] * 1201
    V_fail_buck = [0] * 1201
    for i in range(1201):
        M_fail_ten[i] = FOS['tension'] * max_BMD
        M_fail_comp[i] = FOS['compression'] * max_BMD
        M_fail_buck1[i] = FOS['flexbuck1'] * max_BMD
        M_fail_buck2[i] = FOS['flexbuck2'] * max_BMD
        M_fail_buck3[i] = FOS['flexbuck3'] * max_BMD
        V_fail_shear[i] = FOS['shear'] * max_SFD
        V_fail_glue[i] = FOS['glue'] * max_SFD
        V_fail_buck[i] = FOS['shearbuck'] * max_SFD
    return M_fail_ten, M_fail_comp, M_fail_buck1, M_fail_buck2, M_fail_buck3, V_fail_shear, V_fail_glue, V_fail_buck

if __name__ == '__main__':
    # Beam properties
    L = 1200  # Length of the beam in mm
    n = 1200  # divide in 1 mm
    sigma_ten = 30 # maximum tension stress for matboard
    sigma_comp = 6 # maximum compression stress for matboard
    tau_max = 4 # maximum shear stress for matboard
    tau_glue_max = 2 # maximum shear stress for glue
    E = 4000 # Young’s modulus
    mu = 0.2 # Poisson's ratio
    P = 400   # weight of whole train
    x = np.linspace(0, L, 1201)   # linspace to approximate the beam length
    x_train = [-856, -680, -516, -340, -176, 0]  # distance/length between point loads
    point_loads = [135/2, 135/2, 135/2, 135/2, 182/2, 182/2]
    dx = 1
    SFD = [[] for i in range(2057)]
    BMD = [[] for i in range(2057)]
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
                indices = x >= train_location[i]
                cur_SFD[indices] -= point_loads[i]
        #calculate BMD
        cur_BMD = np.cumsum(cur_SFD) * dx
        # put all SFD and BMD into SFE and BME
        SFD[xj].append(cur_SFD.tolist())
        BMD[xj].append(cur_BMD.tolist())
    #initial sets for maximum SFD and BMD
    SFE = [0] * 1201
    BME = [0] * 1201
    # find maximum SFD and BMD
    BME_dis = 0
    for i in range(1201):
        for xj in range(2057):
            if abs(SFE[i]) <= abs(SFD[xj][0][i]):
                SFE[i] = abs(SFD[xj][0][i])
            if abs(BME[i]) <= abs(BMD[xj][0][i]):
                BME[i] = BMD[xj][0][i]
    max_SFD = SFE[0]
    max_BMD = BME[0]
    for i in range(1201):
        if max_SFD <= SFE[i]:
            max_SFD = SFE[i]
            max_SFD_dis = i
        if max_BMD <= BME[i]:
            max_BMD = BME[i]
            max_BMD_dis = i
    for xj in range(2057):
        if BMD[xj][0][643] == max_BMD:
            print(xj)
            break
    shape_of_design0 = [
    #length(b),height(h),dis of centroid to bot edge(y)
    [120, 1.27, 119.405], # top piece
    [120, 1.27, 118.135], #glue tape
    [5, 1.27, 116.865], #glue tape
    [5, 1.27, 116.865],
    [1.27, 114.96, 58.75],
    [1.27, 114.96, 58.75],
    [75, 1.27, 0.635] #bot piece
    ]
    '''
    -------------------
      --           --
      -             -
      -             -
      -             -
      -             -
      -             -
      ---------------
    '''

    ybar = calculate_ybar(shape_of_design0)
    I = calculate_I(shape_of_design0, ybar)
    Qcent = calculate_Q(shape_of_design0, ybar, ybar)
    Qglue = calculate_Q(shape_of_design0, 117.5, ybar)
    sigma_bot, sigma_top = calculate_flextual_strss(max_BMD, ybar, 120.04, I)
    tau_cent = calculate_tau(max_SFD, Qcent, I, 2.54)
    tau_glue = calculate_tau(max_SFD, Qglue, I, 10)
    sigma_buck1 = calculate_flex_buck(4, E, mu, 2.54, 75)
    sigma_buck2 = calculate_flex_buck(0.425, E, mu, 2.54, 10)
    sigma_buck3 = calculate_flex_buck(6, E, mu, 1.27, 117.5 - ybar)
    tau_buck = calculate_shear_buck(E, mu, 1.27, float('inf'), 117.5)
    FOS = calculate_FOS(sigma_ten, sigma_bot, sigma_comp, sigma_top, sigma_buck1, sigma_buck2, sigma_buck3, tau_max, tau_cent, tau_glue_max, tau_glue, tau_buck)
    M_fail_ten, M_fail_comp, M_fail_buck1, M_fail_buck2, M_fail_buck3, V_fail_shear, V_fail_glue, V_fail_buck = visualize(FOS, max_BMD, max_SFD)
    print("Centroid Axis ybar:", ybar)
    print("Second moment of inertia:", I)
    print("Q at centroid", Qcent)
    print("Q at glue:", Qglue)
    print("Maximum shear force:", max_SFD)
    print("Maximum bending moment:", max_BMD)
    print("Maximum tensile flexural stress:", sigma_bot)
    print("Maximum compressive flexural stress:", sigma_top)
    print("Max shear stress at centroid:", tau_cent)
    print("Max shear stress at glue:", tau_glue)
    print("Top flange middle bucking stress:", sigma_buck1)
    print("Top flange edge bucking stress:", sigma_buck2)
    print("Webs buckling stress:", sigma_buck3)
    print("Shear buckling on webs:", tau_buck)
    print("FOS of different failure mode:",FOS)
    #graphing
    # plotting SFD vs. centroid shear failure
    plt.figure(figsize=(15, 5))
    plt.plot(x, SFE, label='Shear Force V(x)', color='black')
    plt.plot(x, V_fail_shear, label='Centroid Shear Failure', color='red')
    plt.title('Shear Force Envelope')
    plt.xlabel('Position along the beam (mm)')
    plt.ylabel('Shear Force (N)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()

    # plotting SFD vs. glue failure
    plt.figure(figsize=(15, 5))
    plt.plot(x, SFE, label='Shear Force V(x)', color='black')
    plt.plot(x, V_fail_glue, label='Glue Failure', color='red')
    plt.title('Shear Force Envelope')
    plt.xlabel('Position along the beam (mm)')
    plt.ylabel('Shear Force (N)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()

    # plotting SFD vs. web buckling failure
    plt.figure(figsize=(15, 5))
    plt.plot(x, SFE, label='Shear Force V(x)', color='black')
    plt.plot(x, V_fail_buck, label='Web Buckling Failure', color='red')
    plt.title('Shear Force Envelope')
    plt.xlabel('Position along the beam (mm)')
    plt.ylabel('Shear Force (N)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()

    # plotting BMD vs. matboard tension and compression failure
    plt.figure(figsize=(12, 6))
    plt.gca().invert_yaxis()
    plt.plot(x, BME, label='Bending Moment M(x)', color='black')
    plt.plot(x, M_fail_ten, label='Matboard Tension Failure', color='red')
    plt.plot(x, M_fail_comp, label='Matboard Compression Failure', color='green')
    plt.title('Bending Moment Envelope')
    plt.xlabel('Position along the beam (mm)')
    plt.ylabel('Bending Moment (N·mm)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()

    # plotting BMD vs. top flange buckling failure
    plt.figure(figsize=(12, 6))
    plt.gca().invert_yaxis()
    plt.plot(x, BME, label='Bending Moment M(x)', color='black')
    plt.plot(x, M_fail_buck1, label='Top Flange Middle Buckle', color='red')
    plt.plot(x, M_fail_buck2, label='Top Flange Edge Buckle', color='green')
    plt.title('Bending Moment Envelope')
    plt.xlabel('Position along the beam (mm)')
    plt.ylabel('Bending Moment (N·mm)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()

    # plotting BMD vs. web buckling failure
    plt.figure(figsize=(12, 6))
    plt.gca().invert_yaxis()
    plt.plot(x, BME, label='Bending Moment M(x)', color='black')
    plt.plot(x, M_fail_buck3, label='Webs Buckle', color='red')
    plt.title('Bending Moment Envelope')
    plt.xlabel('Position along the beam (mm)')
    plt.ylabel('Bending Moment (N·mm)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()
