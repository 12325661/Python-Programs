def second_smallest_and_greatest_element(arr):
    # Remove duplicates and sort the array
    unique_elements = sorted(set(arr))
    
    # Check if there are fewer than 2 unique elements
    if len(unique_elements) < 2:
        return -1, -1
    
    # Get the second smallest and second largest elements
    second_smallest_element = unique_elements[1]
    second_largest_element = unique_elements[-2]
    
    return second_smallest_element, second_largest_element

# Test arrays
arr1 = [1, 2, 4, 7, 7, 5]
arr2 = [1]

# Testing the function
print(second_smallest_and_greatest_element(arr1))  # Expected: (2, 5)
print(second_smallest_and_greatest_element(arr2))  # Expected: (-1, -1)
