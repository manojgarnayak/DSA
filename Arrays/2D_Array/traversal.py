import numpy as np 

arr2d = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

def traverse(arr2d):
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            print(arr2d[i][j])
traverse(arr2d)