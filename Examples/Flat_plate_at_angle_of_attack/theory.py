#It is the theoric examination of a flat plate at 20 degree angle of attack in a M=3 supersonic flow.
#It can be divided 5 region."
#1-Upstream"
#2-The region after the expansion that is at the top of the plate
#3-The region after the shock that is at the bottom of the plate
#4-The region after the shock that comes after the expansion of the top part
#5-The region after the expansion that comes after the shock of bottom part

import math
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

if project_root not in sys.path:
    sys.path.append(project_root)

from scripts.Gas_Dynamics import prandtl_meyer_eqn
from scripts.Gas_Dynamics import gas_dynamics
from scripts.Gas_Dynamics import theta_beta_M_beta_expilicit_solver
from scripts.Numeric_Methods import hybrid_Root_Solver


M1 = 3
angle_of_attack= 20
gamma = 1.4

#Firstly, the expansion at the top will be solved
#1 ==> 2"

#Alpha value will be omega in the expansion theory
theta = angle_of_attack

#nu value of the region 1 can be calculated. Then nu(M2) and M2 can be found

M2 = prandtl_meyer_eqn.M1_to_M2_expansion_solver(M1,theta)
M2 = M2[0]

p12_ratio = prandtl_meyer_eqn.p1_p2_ratio(M1,M2)

#Secondly, the shock at the bottom can be solved
#Beta value should be founnd first

beta_list = theta_beta_M_beta_expilicit_solver.theta_beta_M_solver(M1,math.radians(angle_of_attack))

#There is no information about backpressure so weak shock can be assumed

beta = math.degrees(min(beta_list))

#Normal Mach Number should be calculated

Mn1 = M1*math.sin(math.radians(beta))

#Pressure ratio and Mn3 can be calculated by using normal shock equations

p31_ratio = gas_dynamics.normal_shock_pressure_ratio(Mn1)

Mn3 = gas_dynamics.normal_shock_mach(Mn1)

M3 = Mn3/math.sin(math.radians(beta-theta))


#An iterative solution should be applied for region 4 and 5
#p4 must be equal to the p5. Otherwise the ab line will move
#phi angle generally quite small (on the order of a degress of less)

#A phi value can be assumed
#It is wrong but close since it is small

#Shock and expansion angle (theta) will be equal to sum of alpha and phi

#The pressure ratio of region 4 and 5 will be calculated based on the assumption
#It will be iterated until p4 = p5

#First consider the shock between region 2 and 4
#Same procedure as previous shock calculation


def phi_func(angle_of_attack,M2,M3,p12_ratio,p31_ratio):
    def f(phi):
        theta_45 = phi + angle_of_attack
        beta24_list = theta_beta_M_beta_expilicit_solver.theta_beta_M_solver(M2,math.radians(theta_45))
        beta24 = math.degrees(min(beta24_list))
        Mn2 = M2*math.sin(math.radians(beta24))
        p42_ratio = gas_dynamics.normal_shock_pressure_ratio(Mn2)
        term1 = p42_ratio/p12_ratio

        M5 = prandtl_meyer_eqn.M1_to_M2_expansion_solver(M3,theta_45)
        M5 = M5[0]
        p35_ratio = prandtl_meyer_eqn.p1_p2_ratio(M3,M5)
        term2 = p31_ratio/p35_ratio

        return term1-term2
    return f


phi = hybrid_Root_Solver.hybrid_root_solver(phi_func(angle_of_attack,M2,M3,p12_ratio,p31_ratio),0,5)
#Phi angle approximately 1 degree


#To find lift and drag p1 and lenght should be known
#Lets assume atmospheric pressure


p1 = 101325
c = 1 #lenght

#Lift
L = (p31_ratio*p1 - p1/p12_ratio)*c*math.cos(math.radians(angle_of_attack))
cL = 2/(gamma*M1**2)*(p31_ratio-1/p12_ratio)*math.cos(math.radians(angle_of_attack))
#Drag
D = (p31_ratio*p1 - p1/p12_ratio)*c*math.sin(math.radians(angle_of_attack))
cD = 2/(gamma*M1**2)*(p31_ratio-1/p12_ratio)*math.sin(math.radians(angle_of_attack))

print(phi)