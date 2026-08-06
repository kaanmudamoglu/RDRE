import sys
import os
import math

# 1. Tell Python to look in the parent 'scripts' directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_scripts_dir = os.path.dirname(current_dir)
sys.path.append(parent_scripts_dir)

# 2. Import your centralized root finder
from Numeric_Methods.hybrid_Root_Solver import hybrid_root_solver


def theta_beta_M(M1, theta, gamma=1.4):

    def f(beta):
        term1 = (
            (2 / math.tan(beta))
            * (
                (M1**2 * math.sin(beta)**2 - 1)
                /
                (M1**2 * (gamma + math.cos(2 * beta)) + 2)
            )
        )

        term2 = math.tan(theta)

        return term1 - term2

    return f


def theta_beta_M_solver(
    M1,
    theta,
    gamma=1.4,
    tolerance=1e-8
):
    
    # The minimum physically possible shock angle is the Mach angle
    mu = math.asin(1 / M1)
    
    f = theta_beta_M(M1, theta, gamma)

    # Search for roots between the Mach angle and a normal shock (pi/2)
    roots = hybrid_root_solver(
        f,
        mu,
        math.pi / 2,
        tolerance=tolerance
    )

    return roots


# ===================================================
# TEST
# ===================================================

#roots = theta_beta_M_solver(
#    3,
#   math.radians(20)
#)

#for root in roots:
#    print(math.degrees(root))