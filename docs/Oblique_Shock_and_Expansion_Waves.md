
# Oblique Shock and Expansion Waves

## Introduction


  <img width="711" height="382" alt="image" src="https://github.com/user-attachments/assets/000fd008-7e0b-4977-a0b5-0378ee1acfaa" />
  
  Oblique shocks usually occur when supersonic flow "is turned into itself". At point A, the surface is deflected upward through an angle $\theta$.  Consequently, the flow streamlines are deflected upward, toward the main bulk of the flow above the surface. This change in flow direction takes place across a shock wave which is oblique to the free-stream direction. All the flow lines experience the same deflection angle $\theta$ at the shock. Hence the flow downstream of the shock is also uniform and parallel, and follows the direction of the wall downstream of point A.

### Across the shock:
- Mach number decreases
- Pressure increases
- Temperature increases
- Density increases

  In contrast, when supersonic flow is "turned away from itself", expansion wave is formed. Here, he surface is deflected downward through an angle $\theta$. Consequently the flow streamlines are deflected downward, away from the main bulk of flow above the surface. This change in flow direction takes place across an expansion wave, centered at point A. Away from the surface, this oblique expansion wave fans out, as shown in Fig. 4.4b. In contrast to the discontinuities across a shock wave, all flow properties through an expansion wave change smoothly and continuously, with the exception of the wall streamline which changes discontinuously at point A.

### Across the expansion wave:
- Mach number increases
- Pressure decreases$
- Temperature decreases
- Density decreases

## Oblique Shock Relations
For an oblique shock, vectoral properties can be divided as normal and tangential ones such as $M_n$ and $M_t$ and $u_1$ (normal velocity) and $\omega_1$ (tangential velocity) . If integral forms of conservation equations are applied to the conrtol volume, 4 equations are obtained:

-Continuity: $\rho_1 u_1 = rho_2 u_2$

-Momentum: $\omega_1 = \omega_2$ and $p_1 + \rho_1 u_1^2 = p_2 + \rho_2 u_2^2$

-Energy: $(h_1 + \frac{V_1^2}{2})\rho_1 u_1 = (h_1 + \frac{V_1^2}{2})\rho_2 u_2$

  If energy equation is divided by continuity:
  $$h_1 + \frac{V_1^2}{2} = h_2 + \frac{V_2^2}{2}$$

  Since $V_1^2 - V_2^2 = (u_1^2 + \omega_1^2) - (u_1^2 + \omega_1^2)$:

  $$h_1 + \frac{u_1^2}{2} = h_2 + \frac{u_2^2}{2}$$

  $$ M_{n_1} = M_1 sin(\beta)$$

### Note:
These equation are identical in form to the normal shock equations so, same equations are valid for normal components of the flow such as $M_2$. Ratios of perssure, density and temperature can be calculated by using same expressions.
$$M_2 = \frac{M_{n_2}}{sin(\beta-\theta)}$$
 
  Changes across an oblique shock are function of both $M_1$ and $\beta$. Normal shocks are just a special case of oblique shocks where $\beta = \pi/2$


  $M_2 cannot be found until the flow deflection angle $\theta$ is obtained. However, $\theta$ is also function of $M_1$ and $\beta$.

$$tan\beta = \frac{u_1}{\omega_1}$$

$$tan(\beta-\theta) = \frac{u_2}{\omega_2}$$

Then, by using continuity, density ratio equation and realation between $M_1$ and $M_{n_1}$:

$$\tan \theta = 2 \cot \beta \left[ \frac{M_1^2 \sin^2 \beta - 1}{M_1^2 (\gamma + \cos 2\beta) + 2} \right]$$

This equation is called $\theta - \beta - M$ relation. This relation is vital to analysis of oblique shocks and results are plotted at below:
<img width="642" height="471" alt="image" src="https://github.com/user-attachments/assets/049a2cd9-a45a-427c-8f41-f70c2c96a4a4" />

### Note

<img width="631" height="357" alt="image" src="https://github.com/user-attachments/assets/3f930865-fdbc-4e1c-a993-a14d7e29f23d" />

- For any given $M_1$, there is a maximum deflection angle $\theta_{max}$. If the geometry such that $\theta > \theta_{max}$, then mo solution exists for a straight oblique shock wave. Instead, the shock will be curved and detached.
-For any given $\theta < \theta_{max}$ there are two values of $beta$ predicted by the equation. The large value of $beta$ is called as strong shock solution and small one is called as weak shock solution. In nature, the weak shock solution is favored. Whether the weak or normal shock occurs determined by backpressure. If the downstream pressure is increased by some independent mechanism than the strong shock can be occur. In the weak shock solution, $M_2$ is supersonic except for a small region near $\theta_{max}$. In the strong shock solution $M_2$ is subsonic.
- If $\theta = 0$ then $\beta = \pi/2$ (corresponding to a normal shock) or $\beta = \mu$
- For fixed $\theta$, as the free stream Mach number decreases the wave angle increases. Finally, there is a Mach number below which is no solution are possible. For lower Mach numbers the shock becomes detached. 

 
  
