
def heated_total_temperature2(c_p, q, T_o1):    
    T_o2 = q/c_p + T_o1

    return T_o2

def M2_funtion(M1, T_o1, T_o2, gamma=1.4):

    def f(M2):
        term1 = (1+gamma*(M1**2))/(1+gamma*(M2**2))
        term2 = (M2**2)/(M1**2)
        term3 = (1+((gamma-1)/2)*(M2**2))/(1+((gamma-1)/2)*(M1**2))
        return (term1**2)*(term2)*term3-T_o2/T_o1


    return f



def heated_M2_sub(M1, T_o1, T_o2, gamma=1.4, tol=1e-8, max_iter=1000):

    f = M2_funtion(M1, T_o1, T_o2, gamma)

    a = M1
    b = 0.999999999

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError(
            "Root is not bracketed in (0,1). "
            f"f(a)={fa}, f(b)={fb}"
        )

    for _ in range(max_iter):

        fa = f(a)
        fb = f(b)

        if abs(fb - fa) > 1e-12:
            x = b - fb * (b - a) / (fb - fa)
        else:
            x = (a + b) / 2

        if not (a < x < b):
            x = (a + b) / 2

        fx = f(x)

        if abs(fx) < tol:
            return x

        if fa * fx < 0:
            b = x
        else:
            a = x

        if abs(b - a) < tol:
            return (a + b) / 2

    raise RuntimeError("Maximum iteration count reached")



def heated_M2_sup(M1, T_o1, T_o2, gamma=1.4, tol=1e-8, max_iter=1000):
    f = M2_funtion(M1, T_o1, T_o2, gamma)

    # In supersonic heating, M2 will always be between 1.0 and M1
    a = 1.000001 # Slightly above 1 to avoid division by zero issues
    b = M1
    
    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        
        # Avoid division by zero in the secant step
        if abs(fb - fa) < 1e-14:
            break
            
        # Secant step
        x = b - fb * (b - a) / (fb - fa)
        fx = f(x)

        # Mathematical definition of a root: the function evaluates to ~0
        if abs(fx) < tol:
            if 1 < x:
                return x
            else:
                print("Something is wrong. M2 dropped below 1.")
                return None
        
        # Shift the points for the next iteration (Crucial Step)
        a = b
        b = x
        
    raise RuntimeError("Maximum iteration count reached in supersonic solver")

def heated_M2_calc():

    m1_input_str = input("Enter upstream Mach Number (M1 > 1.0): ")
    m1_input = float(m1_input_str)

    T_o1_input_str = input("Enter total temperature in Kelvin: ")
    T_o1_input = float(T_o1_input_str)

    q_input_str = input("How much heat is added? q:")
    q_input = float(q_input_str)
    

    c_p = 1005
    T_o2 = heated_total_temperature2(c_p, q_input, T_o1_input)

    gamma_input_str = input("Enter Specific Heat Ratio (gamma) [Press Enter for Air=1.4]: ")
    gamma_input = float(gamma_input_str) if gamma_input_str.strip() else 1.4


    # --- NEW: THERMAL CHOKING LIMIT CHECK ---
    term_a = 2 * (gamma_input + 1) * (m1_input**2)
    term_b = (1 + gamma_input * (m1_input**2))**2
    term_c = 1 + ((gamma_input - 1) / 2) * (m1_input**2)
    
    T_ratio = (term_a / term_b) * term_c
    T_o_star = T_o1_input / T_ratio
    q_max = c_p * (T_o_star - T_o1_input)
    
    if q_input > q_max:
        print("\n" + "!"*50)
        print(" PHYSICAL LIMIT EXCEEDED (THERMAL CHOKING)")
        print("!"*50)
        print(f"The maximum heat that can be added is q* = {q_max:.2f} J/kg")
        print("Adding more heat than this will choke the flow (M2 reaches 1).")
        print("Upstream conditions must change to accommodate this heat.")
        return None
    # ----------------------------------------

    # If the check passes, proceed with calculating T_o2 and running the solver
    T_o2 = heated_total_temperature2(c_p, q_input, T_o1_input)

    settings_input = input("Do you want to change solver settings? (y/n)")
    if settings_input == "y" or settings_input =="Y":
        tol_input_str = input("Tolerance:")
        max_iter_str = input("Max iteration:")
        
        tol_input = float(tol_input_str)
        max_iter_input = float(max_iter_str)
    else:
        tol_input = 1e-8
        max_iter_input = 1000

    if 0<m1_input<1:
        M2 = heated_M2_sub(m1_input,T_o1_input,T_o2,gamma_input,tol_input,max_iter_input)
        return M2
    
    elif m1_input>1:
        M2 = heated_M2_sup(m1_input,T_o1_input,T_o2,gamma_input,tol_input,max_iter_input)
        return M2
    
    elif m1_input == 1:
        print("More heat addition cannot be solved in this formulas")

    else:
        print("M1 input shoul be an integer value higher than 0")





print(heated_M2_calc())


