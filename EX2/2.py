import time
import numpy as np
import matplotlib.pyplot as plt


#section 2
# Function to compute the inner product of two matrices
def inner_product(a, b):
    return np.trace(np.dot(a.T.conjugate(), b))


#section 2
# Function to calculate normalized inner product (cosine similarity)
def norm_1(a, b):
    """
    Calculates the normalized inner product between matrices a and b.
    If either matrix has a zero norm, returns 0.
    """
    a_norm = np.sqrt(inner_product(a, a))
    b_norm = np.sqrt(inner_product(b, b))
    if a_norm == 0 or b_norm == 0:
        return 0
    return inner_product(a, b) / (a_norm * b_norm)


if __name__ == '__main__':
    # Section 1: Create and display a template "face" as a 14x14 matrix
    x = np.zeros([14, 14])
    x[3, 2:6] = 1

    x[4, [3, 4, 9, 10]] = 1
    x[3, 8:12] = 1
    x[6:10, 6:8] = 1
    x[9, 5:9] = 1
    x[10:12, 3::7] = 1
    x[12, 3:11] = 1
    plt.imshow(x, cmap='gray')
    plt.title('2_1 part a')

    plt.show()
    time.sleep(1)
    Y = 1-x
    plt.title('2_1 part b')

    plt.imshow(Y, cmap='gray')
    plt.show()
    time.sleep(1)
    # Section 3: Iteratively test random "faces" against the template
    ipN = 0
    Th = 0.59
    L = 14
    j = 0
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    Xtest = np.zeros([L, L])
    while ipN < Th: # Continue until similarity meets or exceeds threshold
        Xtest[2:L-1, 2:L-1] = np.random.randint(0, 2, [L - 3, L - 3])
        ipN = norm_1(x, Xtest)
        j += 1
        if ipN >= Th:
            print('ipN = ', ipN, 'access permitted')
        else:
            print('ipN = ', ipN, 'access denied')

    axes[0].imshow(Xtest, cmap='gray')
    axes[0].set_title(f'{ipN:.2f} test face')

    axes[1].imshow(x, cmap='gray')
    axes[1].set_title('template face')
    plt.tight_layout()
    plt.show()
    time.sleep(1)
    print(f"Number of iterations: {j}")


