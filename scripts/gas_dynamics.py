import math

# ==========================================
# CORE: Pure Mathematical Solvers
# ==========================================

def normal_shock_mach(M1, gamma=1.4):
    """
    Calculates downstream Mach number (M2) across a normal shock.
    """
    if M1 <= 1.0:
        raise ValueError("Normal shocks only occur in supersonic flow (M1 > 1.0).")
    
    numerator = 1 + ((gamma - 1) / 2) * (M1**2)
    denominator = gamma * (M1**2) - ((gamma - 1) / 2)
    M2 = math.sqrt(numerator / denominator)
    return M2

def normal_shock_pressure_ratio(M1, gamma=1.4):
    """
    Calculates static pressure ratio (p2/p1) across a normal shock.
    """
    if M1 <= 1.0:
        raise ValueError("Normal shocks only occur in supersonic flow (M1 > 1.0).")
        
    p_ratio = 1 + (2 * gamma / (gamma + 1)) * ((M1**2) - 1)
    return p_ratio

def normal_shock_temperature_ratio(M1, gamma=1.4):
    """
    Calculates static temperature ratio (T2/T1) across a normal shock.
    """
    if M1 <= 1.0:
        raise ValueError("Normal shocks only occur in supersonic flow (M1 > 1.0).")
        
    term1 = 1 + (2 * gamma / (gamma + 1)) * ((M1**2) - 1)
    term2 = (2 + (gamma - 1) * (M1**2)) / ((gamma + 1) * (M1**2))
    t_ratio = term1 * term2
    return t_ratio


# ==========================================
# SHELL: Interface and Execution Layout
# ==========================================

def run_shock_calculator():
    """
    Handles user interaction, gathers inputs, and displays formatted results.
    """
    print("\n" + "="*45)
    print(" 1D Gas Dynamics: Normal Shock Calculator")
    print("="*45)
    
    try:
        # Gather Inputs
        m1_input_str = input("Enter upstream Mach Number (M1 > 1.0): ")
        m1_input = float(m1_input_str)
        
        gamma_input_str = input("Enter Specific Heat Ratio (gamma) [Press Enter for Air=1.4]: ")
        gamma_input = float(gamma_input_str) if gamma_input_str.strip() else 1.4

        # Execute Core Functions
        m2 = normal_shock_mach(m1_input, gamma_input)
        p_ratio = normal_shock_pressure_ratio(m1_input, gamma_input)
        t_ratio = normal_shock_temperature_ratio(m1_input, gamma_input)

        # Display Formatted Outputs
        print("\n" + "-"*20 + " RESULTS " + "-"*20)
        print(f"Downstream Mach (M2):      {m2:.4f}")
        print(f"Pressure Ratio (p2/p1):    {p_ratio:.4f}")
        print(f"Temperature Ratio (T2/T1): {t_ratio:.4f}")
        print("-"*49 + "\n")

    except ValueError as e:
        print(f"\n[!] Input Error: {e}\n")

if __name__ == "__main__":
    run_shock_calculator()
