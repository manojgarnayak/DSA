import numpy as np 

arr2d = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

def accessElements(arr2d, rowInd, colInd):
    if rowInd >= len(arr2d) and colInd >= len(arr2d[0]):
        print("Incorrect Index")
    else:
        print(arr2d[rowInd][colInd])

accessElements(arr2d, 1, 3)