# Module 1: Compressible Flow Fundamentals

## 1. Introduction and Assumptions
Compressible Flow can be defined as variable density flow which is in constrast to incompressible flow. Consider small element of fluid of volume $v$. The pressure around the element is $p$. Assume pressure is increased by an infinitesimal $dp$. Naturally, volume changes $dv$ amonut. The volume change per unit volume can be expressed as $\frac{dv}{v}$. The fractioanl volume change per unit pressure shange which is called compressibility can be expressed as:
  
  $$\tau = \frac{-dv/v}{dp}$$

If fluid has unit mass that $\rho = 1/v$. Then expression can be rearranged as:

$$\tau = \frac{1}{\rho} \frac{d\rho}{dp}$$

For most practical problems, the flow is considered as compressible if $d\rho/\rho$ is more than 5 percent.

The gas assumed as continuum, perfect and inviscid for most of the cases.

$$p = \rho R T$$

$$R = 287 \frac{J}{kg * K}$$

$$ \gamma= \frac{c_p}{c_v} $$

## 2. Speed of Sound and Mach Number
The speed of sound is the speed at which a small pressure wave propagates through a fluid. For an ideal gas, it depends entirely on the temperature.

* **Speed of Sound ($a$):**
  $$a = \sqrt{\gamma R T}$$
  Where $\gamma$ is the specific heat ratio, $R$ is the specific gas constant, and $T$ is the static temperature.

* **Mach Number ($M$):**
  $$M = \frac{V}{a}$$
  Where $V$ is the local flow velocity.

  $M<0.8$ subsonic flow

  $0.8<M<1.2$ transonic flow

  $1<M$ supesonic flow

## 3. Isentropic Relations

An isentropic process was already defined as adiabatic and reversible. 

$$\partial{q}=0$$ 
$$ds_i=0  $$
$$ds=0 $$
$$\frac{p_2}{p_1}=\left(\frac{\rho_2}{\rho_1}\right)^\gamma=\left(\frac{T_2}{T_1}\right)^\frac{\gamma}{\gamma-1}$$

  
## 4. Stagnation (Total) Properties vs. Static Properties

The fundamental isentropic relations linking total properties (denoted with subscript $0$) to static properties are:

* **Temperature Ratio:**
  $$\frac{T_0}{T} = 1 + \frac{\gamma - 1}{2} M^2$$

* **Pressure Ratio:**
  $$\frac{p_0}{p} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{\gamma}{\gamma - 1}}$$

* **Density Ratio:**
  $$\frac{\rho_0}{\rho} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{1}{\gamma - 1}}$$

  #  One-Dimensional Flow:
  The normal shock waves will be investigated. Because of the asuumption of 1-D flow, flow field properties are function of $x$ only. Assume that the left and right sides easch have an area equal to the $A$ perperndicular the flow and flow is steady.

  Condisedring continuity equation:

$$\rho_1 u_1 = \rho_2 u_2$$

  The momentum equation:

$$\int \rho_1 (\vec{u}_1 \cdot \vec{n}) \,dA_1 + \int \rho_2 (\vec{u}_2 \cdot \vec{n}) \,dA_2 = p_1 A_1 -p_2 A_2$$

$$ p_1 + \rho_1 u_1^2 = p_2 + \rho_2 u_2^2$$

  Energy Equation is reduced to:
  
  $$h_1 + \frac{u_1^2}{2} + q = h_2 + \frac{u_2^2}{2}$$


  ## Some Conveniently Defined Flow Parameters

  Consider point $A$ in an arbitrary flowfield.  At this point a fluid element is traveling at some $M$, $V$, with a static pressure and temperature $p$ and $T$. Take this element and adiabaticly slow it down (if $M>1$) or speed it up (if $M<1$) until its Mach numver at point A is 1. As we do this, temperature will change which will be indicated as $T^\star$. Furthermore, the speed of sound at this hypothetical Mach 1 condition as $a^\star=\sqrt{\gamma R T^\star}$. 

  Consider again our fluid element with $V$, $T$, and $p$. Isentropically slow this fluid element to zero velocity. The pressure and velocity defined as total pressure $p_0$ and total temperature $T_0$, respectively. They are fraquently called as stagnation pressure and temperature. The actual $p$ and $T$ (while element is moving) are called static pressure and static temperature.

  Using these definitions, other parameters can be introduced:

  Characterictic Mach Number : $M^\star = V/a^\star$

  Stagnation speed of sound : $a_0 = \sqrt{\gamma R T_0}$

  Total density : $\rho_0 = p_0/RT_0$


  $$\frac{a^2}{\gamma-1} + \frac{u^2}{2} = \frac{\gamma+1}{2(\gamma-1)}(a^\star)^2$$


  $$\frac{T_o}{T} = 1 + \frac{\gamma - 1}{2} M^2$$

  $$\frac{p_o}{p} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\gamma / (\gamma - 1)}$$

  $$\frac{\rho_o}{\rho} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{1 / (\gamma - 1)}$$






