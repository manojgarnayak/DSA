import array

arr = array.array('i',[1,2,3,4,5])

def accessElement(arr,index):
    if index >= len(arr):
        print("Error please check again!")
    else:
        print(arr[index])

accessElement(arr,5)