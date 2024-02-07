import array

# Create an array and traverse
arr = array.array('i', [10,20,30,40,50])
for i in arr:
    print(i)


# Access individual elements indexes
print(arr[4])


# Append any value to the array using append() method
arr.append(60)
print(arr)


# Insert value in an array using insert() method
arr.insert(5,70)
print(arr)


# Extend python array using extend() method
my_arr = array.array('i',[11,22,33,44,55])
arr.extend(my_arr)
print(arr)


# Add items form list into array using fromlist() method
templist = [11,12,13,14,15]
arr.fromlist(templist)
print(arr)


# Remove any array element using remove() method
arr.remove(40)
print(arr)


# Remove last array element using pop() method
arr.pop()
print(arr)


# Fetch any element through its index using index() method
print(arr.index(30))


# Reverse a Python array using reverse() method
arr.reverse()
print(arr)


# Get reverse buffer information through buffer_info() method
print(arr.buffer_info())


# Check for number of occurences of an element using count() method
print(arr.count(20))


# Convert array to string using tobytes() or frombytes() method
# Append a string to char array using fromstring() method
strArr = arr.tobytes()
print(str)


# Convert array to a python list with some elements using tolist() method
print(arr.tolist())


# Slice elements form an array
print(arr[1:3])

