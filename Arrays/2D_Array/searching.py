import numpy as np 

arr2d = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

def searchElement(arr2d, ele):
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            if arr2d[i][j] == ele:
                return "The value is located at index "+ str(i)+ " " + str(j)
    return "The element is not found"

print(searchElement(arr2d, 17))