import numpy as np
in_arr = np.array([[ 2, 0, 1], [ 5, 4, 3], [10,11,6]])
print ("Input array :\n", in_arr)
out_arr1 = np.sort(in_arr)
print ("\nOutput sorted array", out_arr1)
in_arr = np.array([[ 2, 0, 1], [ 5, 4, 3], [10,11,6]])
a=np.where(in_arr>3)
print("\nOutput for where ",a)
