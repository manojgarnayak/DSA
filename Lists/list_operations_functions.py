a = [1,2,3]
b = [4,5,6]
# print(a+b)


c = [1,2]
# print (c * 5)


lst = [1,2,3,4,5]
# print(len(lst))

# print(max(lst))

# print(min(lst))

# print(sum(lst))

# print(sum(lst)/len(lst))

mylist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    mylist.append(value)
average = sum(mylist) / len(mylist)

print('Average: ', average)