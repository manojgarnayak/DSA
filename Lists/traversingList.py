shoppingList = ["milk","paneer","butter"]
print(shoppingList[1])

# print('milk' in shoppingList)

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList)