import numpy as np

def find_mean_var_std():
    input_arr=input().split()
    n=int(input_arr[0])
    m=int(input_arr[1])
    arr = []

    for _ in range(n):
        arr.append([*map(int, input().split())])
    arr = np.array(arr)

    return ((np.mean(arr,axis=1)))
    return((np.var(arr,axis=0)))
    return(round(np.std(arr,axis = None),11))
