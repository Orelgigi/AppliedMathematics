import numpy as np


def normip(v, p):
    """
    function to compute the natural norm of an input vector.
    Inputs: v - a numpy array (n dim vector), p - real number >=1,
    if p = 'max' the infinity norm is computed (norma ∞).
    Outputs: p norm of v
    """
    if p == "max":
        norm = np.max(np.abs(v))
    else:
        norm = np.pow(np.sum(np.pow(np.abs(v), p)), 1 / p)
    return norm


if __name__ == '__main__':
    # Section 1: Calculate p-norms for a vector
    vec1 = np.array([1j, 2j, -3, 1, 7 - 3j])
    print("norn 2 for v=", normip(vec1, 2))
    print("norn 9 for v=", normip(vec1, 9))
    # Section 2: Normalize a vector
    vec2 = np.array([1j, 5, 2 - 3j, -1+1j, 2j])
    norm_v = normip(vec2, 2)
    print("Unit vector :", vec2 / norm_v)
    # Section 3: Calculate distances between two vectors
    vec3 = np.array([6j, 7, 2, 2j, 7])
    vec4 = np.array([2, 1, -3j, -3, 9])
    print("distance, p=2:", normip(vec3 - vec4, 2))
    print("distance, p=infinity:", normip(vec3 - vec4, "max"))
