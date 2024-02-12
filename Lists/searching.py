mylist = [10,20,30,40,50,60,70,80,90,100]

# target = 50
# if target in mylist:
#     print(f" {target} is in the list")
# else:
#     print(f"{target} is not in the list")


# linear search
    
def search(mylist, ele):
    for i, value in enumerate(mylist):
        if value == ele:
            return i
    return -1

print(search(mylist,50))