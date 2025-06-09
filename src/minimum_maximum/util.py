import numpy as np

'''def min_max(arr):
    arr = np.array(arr)
    return(np.max(np.min(arr,axis=1)))'''
def min_max(arr):

    arr = np.array(arr)
    row_minima = np.min(arr, axis=1)  # Calculate the minimum of each row
    max_of_minima = np.max(row_minima)  # Calculate the maximum of those minima
    return max_of_minima
