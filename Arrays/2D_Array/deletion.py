import numpy as np 

arr2d = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

newArr = np.delete(arr2d,0,axis=0)
print(newArr)
newArr = np.delete(arr2d,0,axis=1)
print(newArr)