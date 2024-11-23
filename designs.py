    #First design
    shape_of_design0 = [
    #length(b),height(h),dis of centroid to bot edge(y)
    [100, 1.27, 99.365],
    [5, 1.27, 98.095],
    [5, 1.27, 98.095],
    [1.27, 5, 96.23],
    [1.27, 5, 96.23],
    [1.27, 97.46, 50],
    [1.27, 97.46, 50],
    [75, 1.27, 0.635]
    ]
    ybar = calculate_ybar(shape_of_design0)
    I = calculate_I(shape_of_design0, ybar)
    Qcent = calculate_Q(shape_of_design0, ybar, ybar)
    Qglue = calculate_Q(shape_of_design0, 96.23, ybar)
    sigma_bot, sigma_top = calculate_flextual_strss(max_BMD, ybar, 100, I)
    tau_cent = calculate_tau(max_SFD, Qcent, I, 2.54)
    tau_glue = calculate_tau(max_SFD, Qglue, I, 2.54)
    sigma_buck1 = calculate_flex_buck(4, E, mu, 1.27, 75)
    sigma_buck2 = calculate_flex_buck(0.425, E, mu, 1.27, 5)
    sigma_buck3 = calculate_flex_buck(6, E, mu, 1.27, 98.73 - ybar)
    tau_buck = calculate_shear_buck(E, mu, 1.27, float('inf'), 98.73)
    
    #Second design
    shape_of_design0 = [
    #length(b),height(h),dis of centroid to bot edge(y)
    [120, 1.27, 99.365], # top piece
    [120, 1.27, 98.095],
    [120, 1.27, 96.825],
    [5, 1.27, 95.565],
    [5, 1.27, 95.565],
    [1.27, 93.66, 48.1],
    [1.27, 93.66, 48.1],
    [75, 1.27, 0.635]
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
    Qglue = calculate_Q(shape_of_design0, 96.2, ybar)
    sigma_bot, sigma_top = calculate_flextual_strss(max_BMD, ybar, 100, I)
    tau_cent = calculate_tau(max_SFD, Qcent, I, 2.54)
    tau_glue = calculate_tau(max_SFD, Qglue, I, 10)
    sigma_buck1 = calculate_flex_buck(4, E, mu, 2.54, 75)
    sigma_buck2 = calculate_flex_buck(0.425, E, mu, 2.54, 12.5)
    sigma_buck3 = calculate_flex_buck(6, E, mu, 1.27, 96.2 - ybar)
    tau_buck = calculate_shear_buck(E, mu, 1.27, float('inf'), 96.2)

    #Third design
    shape_of_design0 = [
    #length(b),height(h),dis of centroid to bot edge(y)
    [120, 1.27, 99.4055], # top piece
    [120, 1.27, 98.135],
    [5, 1.27, 96.865],
    [5, 1.27, 96.865],
    [3.73, 1.27, 95.555],
    [3.73, 1.27, 95.555],
    [1.27, 96.19, 49.365],
    [1.27, 96.19, 49.365],
    [1.27, 94.92, 49.365],
    [1.27, 94.92, 49.365],
    [75, 1.27, 0.635]
    ]
    ybar = calculate_ybar(shape_of_design0)
    I = calculate_I(shape_of_design0, ybar)
    Qcent = calculate_Q(shape_of_design0, ybar, ybar)
    Qglue = calculate_Q(shape_of_design0, 96.19, ybar)
    sigma_bot, sigma_top = calculate_flextual_strss(max_BMD, ybar, 100, I)
    tau_cent = calculate_tau(max_SFD, Qcent, I, 2.54)
    tau_glue = calculate_tau(max_SFD, Qglue, I, 7.46)
    sigma_buck1 = calculate_flex_buck(4, E, mu, 2.54, 75)
    sigma_buck2 = calculate_flex_buck(0.425, E, mu, 2.54, 12.5)
    sigma_buck3 = calculate_flex_buck(6, E, mu, 1.27, 97.46 - ybar)
    tau_buck = calculate_shear_buck(E, mu, 1.27, float('inf'), 97.46)

    #Fourth design

    
    #Fifth design
    shape_of_design0 = [
    #length(b),height(h),dis of centroid to bot edge(y)
    [120, 1.27, 99.4055], # top piece
    [120, 1.27, 98.135],
    [5, 1.27, 96.865],
    [5, 1.27, 96.865],
    [1.27, 94.96, 48.75],
    [1.27, 94.96, 48.75],
    [75, 1.27, 0.635]
    ]
    ybar = calculate_ybar(shape_of_design0)
    I = calculate_I(shape_of_design0, ybar)
    Qcent = calculate_Q(shape_of_design0, ybar, ybar)
    Qglue = calculate_Q(shape_of_design0, 97.5, ybar)
    sigma_bot, sigma_top = calculate_flextual_strss(max_BMD, ybar, 100.04, I)
    tau_cent = calculate_tau(max_SFD, Qcent, I, 2.54)
    tau_glue = calculate_tau(max_SFD, Qglue, I, 10)
    sigma_buck1 = calculate_flex_buck(4, E, mu, 2.54, 75)
    sigma_buck2 = calculate_flex_buck(0.425, E, mu, 2.54, 22.5)
    sigma_buck3 = calculate_flex_buck(6, E, mu, 1.27, 97.5 - ybar)
    tau_buck = calculate_shear_buck(E, mu, 1.27, float('inf'), 97.5)

    # Sixth design
    shape_of_design0 = [
    #length(b),height(h),dis of centroid to bot edge(y)
    [120, 1.27, 119.405], # top piece
    [120, 1.27, 118.135],
    [5, 1.27, 116.865],
    [5, 1.27, 116.865],
    [1.27, 114.96, 58.75],
    [1.27, 114.96, 58.75],
    [75, 1.27, 0.635]
    ]
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
