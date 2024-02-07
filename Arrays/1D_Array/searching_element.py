import array

arr = array.array('i',[1,2,3,4,5,6])
def searchElement(arr,ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1

print(searchElement(arr,8))