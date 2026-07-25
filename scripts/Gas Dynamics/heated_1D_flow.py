import sys
import os
import math

# 1. Tell Python to look in the parent 'scripts' directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_scripts_dir = os.path.dirname(current_dir)
sys.path.append(parent_scripts_dir)

# 2. Correctly import the function from the file inside the folder
# Syntax: from FolderName.FileName import function_name
from Numeric_Methods.hybrid_Root_Solver import hybrid_root_solver


def heated_total_temperature2(c_p, q, T_o1):
    return T_o1 + q / c_p


def M2_function(M1, T_o1, T_o2, gamma=1.4):

    def f(M2):

        term1 = (
            (1 + gamma * M1**2)
            /
            (1 + gamma * M2**2)
        )

        term2 = (
            M2**2
            /
            M1**2
        )

        term3 = (
            (1 + ((gamma - 1) / 2) * M2**2)
            /
            (1 + ((gamma - 1) / 2) * M1**2)
        )

        return (
            term1**2
            * term2
            * term3
            - T_o2 / T_o1
        )

    return f


def heated_M2(
    M1,
    T_o1,
    T_o2,
    gamma=1.4,
    tolerance=1e-8
):

    f = M2_function(
        M1,
        T_o1,
        T_o2,
        gamma
    )

    if M1 < 1:

        roots = hybrid_root_solver(
            f,
            M1,
            0.999999,
            tolerance=tolerance
        )

        return roots[0]

    if M1 > 1:

        roots = hybrid_root_solver(
            f,
            1.000001,
            M1,
            tolerance=tolerance
        )

        return roots[0]

    raise ValueError(
        "M1 = 1 corresponds to sonic flow."
    )

def thermal_choking_limit(
        M1,
        T_o1,
        gamma=1.4,
        c_p=1005):

    term_a = (
        2
        * (gamma + 1)
        * M1**2
    )

    term_b = (
        1
        + gamma * M1**2
    )**2

    term_c = (
        1
        + (gamma - 1)
        / 2
        * M1**2
    )

    T_ratio = (
        term_a
        /
        term_b
        * term_c
    )

    T_o_star = T_o1 / T_ratio

    q_max = c_p * (T_o_star - T_o1)

    return q_max

