import numpy as np
import math


def theta_beta_M(M1, theta, gamma):

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
    gamma,
    tolerance=1e-8,
    max_iter=100
):

    mu = math.asin(1 / M1)

    interval = np.linspace(
        mu + 1e-6,
        math.pi / 2 - 1e-6,
        500
    )

    f = theta_beta_M(M1, theta, gamma)

    roots = []

    beta_old = interval[0]
    fi_old = f(beta_old)

    for beta in interval[1:]:

        fi = f(beta)


        if fi * fi_old < 0:

            left = beta_old
            right = beta

            f_left = fi_old
            f_right = fi

            for _ in range(max_iter):

                # Secant

                if abs(f_right - f_left) > 1e-12:

                    x = right - (
                        f_right
                        * (right - left)
                        / (f_right - f_left)
                    )

                else:
                    x = 0.5 * (left + right)

                # Bracket dışına çıkarsa bisection

                if not (left < x < right):
                    x = 0.5 * (left + right)

                fx = f(x)

                if abs(fx) < tolerance:
                    roots.append(x)
                    break

                if f_left * fx < 0:

                    right = x
                    f_right = fx

                else:

                    left = x
                    f_left = fx

                if abs(right - left) < tolerance:

                    roots.append(
                        0.5 * (left + right)
                    )

                    break

        beta_old = beta
        fi_old = fi

    return roots

roots = theta_beta_M_solver(
    2,
    math.radians(10),
    1.4
)

for root in roots:
    print(math.degrees(root))