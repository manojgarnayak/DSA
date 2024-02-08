import numpy as np 

arr2d = np.array([[1,10,11],[5,4,10],[24,50,37]])
new2darr = np.insert(arr2d,0,[[1,2,3]],axis=0) #axis=0 means a row
new2darr = np.insert(arr2d,0,[[4,5,6]],axis=1) #axis=1 means a column
new2darr = np.append(arr2d, [[7,8,9]], axis=0)
print(new2darr)