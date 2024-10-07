def remove_duplicate(arr):
    # Use a set to store unique elements
    unique_elements = set()

    # Traverse the array and add elements to the set
    for num in arr:
        unique_elements.add(num)

    # Store the size of the unique elements (this is the number of unique elements)
    k = len(unique_elements)

    # Copy the unique elements back to the original array
    i = 0
    for num in unique_elements:
        arr[i] = num
        i += 1

    # Return the number of unique elements
    return k

# Example usage
arr1 = [1, 1, 2, 2, 2, 3, 3]
k = remove_duplicate(arr1)
print("Number of unique elements:", k)
print("Array after removing duplicates:", arr1[:k])
