import numpy as np

def find_linear_algebra():
    num = int(input())
    val = []
    for _ in range(num):
        number = input().split()
        float_value = []
        for x in number:
            float_value.append(float(x))
        val.append(float_value)
    A = np.array(val)

    return(round(np.linalg.det(A), 2))


