import numpy as np


# Question 2
def innerProd(m1: np.ndarray, m2: np.ndarray):
    if m1.shape != m2.shape:
        return str("vector " + str(m1.shape) + " not equal to vector " + str(m2.shape))
    return np.vdot(m2, m1)


if __name__ == '__main__':
    u = np.array([1, 1 - 1j, 2])
    v = np.array([-1, 1 + 1j, 1j])
    w = np.array([-1, 1 - 1j, 2j])
    print("<u,v>:", innerProd(u, v))
    print("<u,w>:", innerProd(u, w))
    print("<v,w>:", innerProd(v, w))
    print("<v,u>:", innerProd(v, u))
    if u.shape == w.shape:
        print("<2u+w,v>:", innerProd(2 * u + w, v))
    else:
        print("<u,w>: vector " + str(u.shape) + " not equal to vector " + str(w.shape))
