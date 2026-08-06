import numpy as np

def hybrid_root_solver(f, a, b, tolerance=1e-8, max_iter=1000, scan_points=1000):
    roots = []
    
    # Boundary offsets validated for singularity avoidance
    interval = np.linspace(a + 1e-6, b - 1e-6, scan_points)
    
    x_old = interval[0]
    f_old = f(x_old)

    for x in interval[1:]:
        fx = f(x)
        
        if (fx * f_old < 0) or (abs(fx) < tolerance):
            left, right = x_old, x
            f_left, f_right = f_old, fx
            
            for _ in range(max_iter):
                # Secant leap
                if abs(f_right - f_left) > 1e-12:
                    x_new = right - f_right * (right - left) / (f_right - f_left)
                else:
                    x_new = 0.5 * (left + right)
                    
                # Strict Bisection fallback
                if not (min(left, right) <= x_new <= max(left, right)):
                    x_new = 0.5 * (left + right)
                    
                f_new = f(x_new)
                
                if abs(f_new) < tolerance:
                    roots.append(x_new)
                    break
                    
                if f_left * f_new < 0:
                    right, f_right = x_new, f_new
                else:
                    left, f_left = x_new, f_new
                    
                if abs(right - left) < tolerance:
                    roots.append(0.5 * (left + right))
                    break

        x_old, f_old = x, fx

    if not roots:
        raise RuntimeError("No roots found in given interval.")
        
    # Transformation: Vectorized and robust duplicate cleanup
    roots = np.sort(roots)
    clean_roots = [roots[0]]
    
    for r in roots[1:]:
        if not np.isclose(r, clean_roots[-1], atol=tolerance):
            clean_roots.append(r)

    return clean_roots

