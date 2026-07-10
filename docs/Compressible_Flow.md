# Module 1: Compressible Flow Fundamentals

## 1. Introduction and Assumptions
*Write a brief summary here about what makes a flow "compressible" (usually when Mach number > 0.3) and the assumption of Isentropic Flow (adiabatic and reversible).*

## 2. Speed of Sound and Mach Number
The speed of sound is the speed at which a small pressure wave propagates through a fluid. For an ideal gas, it depends entirely on the temperature.

* **Speed of Sound ($a$):**
  $$a = \sqrt{\gamma R T}$$
  Where $\gamma$ is the specific heat ratio, $R$ is the specific gas constant, and $T$ is the static temperature.

* **Mach Number ($M$):**
  $$M = \frac{V}{a}$$
  Where $V$ is the local flow velocity.

## 3. Stagnation (Total) Properties vs. Static Properties
*Write a short note here explaining the difference between static pressure (what you feel moving with the flow) and stagnation pressure (what you feel if you bring the flow to a dead stop).*

The fundamental isentropic relations linking total properties (denoted with subscript $0$) to static properties are:

* **Temperature Ratio:**
  $$\frac{T_0}{T} = 1 + \frac{\gamma - 1}{2} M^2$$

* **Pressure Ratio:**
  $$\frac{p_0}{p} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{\gamma}{\gamma - 1}}$$

* **Density Ratio:**
  $$\frac{\rho_0}{\rho} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{1}{\gamma - 1}}$$

## 4. Choked Flow and Mass Flow Rate (Critical for Injector Design)
*Explain "Choking" here. What happens when the flow reaches $M = 1$ at the throat of an injector? Why can't the mass flow rate increase any further even if we drop the downstream pressure?*

The maximum (choked) mass flow rate through an orifice area ($A^*$) is calculated as:
$$\dot{m} = \frac{A^* p_0}{\sqrt{R T_0}} \sqrt{\gamma \left(\frac{2}{\gamma + 1}\right)^{\frac{\gamma + 1}{\gamma - 1}}}$$

This equation is the holy grail for our RDRE injector design. It will dictate exactly how big we need to make our injection holes to achieve the desired mass flow rate.
