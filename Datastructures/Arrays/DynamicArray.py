# Creating an array
arr = [1, 2, 3, 4, 5]

# Accessing elements
print(arr[0])  # Output: 1

# Adding elements
arr.append(6)  # Add to end
arr.insert(2, 99)  # Insert at index 2

# Removing elements
arr.remove(4)  # Removes the value 4
popped_value = arr.pop()  # Removes and returns last element

# Traversing the array
for elem in arr:
    print(elem)