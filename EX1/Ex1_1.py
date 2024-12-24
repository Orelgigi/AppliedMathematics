import numpy as np

# Question 1
a = np.array([[1, 1, 0], [1, -2, 1], [2, 1, 2]])
b = np.array([[1, -1, 1], [-1, 0, 1], [3, 2, 1]])
c = np.array([[1, -1j], [-1, 1j], [0, 2j]])
x = np.array([[1], [2], [-2]])
y = np.array([[2, -1, 3]])


def matrix(m1: np.ndarray, m2: np.ndarray):
    if len(m1[0]) == len(m2):
        return np.dot(m1, m2)
    return str("not size ok (" + str(len(m1[0])) + " , " + str(len(m2)) + ")")


#  Question 1 Section 1
bx = matrix(b, x)
if type(bx) != str:
    bxc = matrix(bx, c)
else:
    bxc = str("BxC : not size ok (" + str(len(b[0])) + " , " + str(len(x)) + ")")
abx = matrix(a, bx)
yyT = matrix(y, y.T)
if type(yyT) != str:
    yyTx = matrix(yyT, x)
else:
    yyTx = str("yyTx : not size ok (" + str(len(y[0])) + " , " + str(len(y.T)) + ")")
abx = matrix(a, bx)
xy = matrix(x, y)
print(" Bx :", str(bx), "BxC :", bxc, "ABx :", str(abx), "yyTx : ", yyTx, "XY :", str(xy), sep="\n")


# Question 1 Section 2
def sumMatrix(m1: np.ndarray, m2: np.ndarray):
    ab = matrix(m1, m2)
    if type(ab) != str:
        return np.sum(ab)
    return ab


def sumMatrix2(m1: np.ndarray, m2: np.ndarray):
    try:
        return np.sum(np.matmul(m1, m2))
    except:
        return str("not size ok (" + str(len(m1[0])) + " , " + str(len(m2)) + ")")


print("sum matrix 1:  " + str(sumMatrix(a, b)))
print("sum matrix 2:  " + str(sumMatrix2(a, b)))
