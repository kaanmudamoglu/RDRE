"The aim of the code is found values of M_2 and v(M_2)"

import sys
import os
import math
# 1. Tell Python to look in the parent 'scripts' directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_scripts_dir = os.path.dirname(current_dir)
sys.path.append(parent_scripts_dir)

# 2. Import your centralized root finder
from Numeric_Methods.hybrid_Root_Solver import hybrid_root_solver

def v_M2(M1,theta, gamma=1.4):
    theta = math.radians(theta)
    v_M1 = math.sqrt((gamma+1)/(gamma-1))*math.atan(math.sqrt((gamma-1)*(M1**2-1)/(gamma+1)))-math.atan(math.sqrt(M1**2-1))
    v_M2 = v_M1 + theta
    v_M2 = math.degrees(v_M2)

    return v_M2

def v_to_M2(v_M2,gamma=1.4):
    vM2 = math.radians(v_M2)
    def f(M2):
        term1 = math.sqrt((gamma+1)/(gamma-1))*math.atan(math.sqrt((gamma-1)*(M2**2-1)/(gamma+1)))-math.atan(math.sqrt(M2**2-1))
        term2 = vM2
        return term1 - term2

    return f

def M1_to_M2_expansion_solver(M1,theta,gamma=1.4):
    vM2 = v_M2(M1,theta,gamma)
    f = v_to_M2(vM2,gamma)

    roots = hybrid_root_solver(f,M1,100000000)

    return roots

