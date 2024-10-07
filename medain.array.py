def median_array(arr):
    arr.sort()  # Sort the array
    n = len(arr)  # Get the number of elements
    if n % 2 == 1:
        # If odd, return the middle element
        median = arr[n // 2]
    else:
        # If even, return the average of the two middle elements
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    return median  # Return the median

arr1 = [2, 4, 1, 3, 5]
print(median_array(arr1))  # Output: 3
arr2 =[2,5,1,7]
print(median_array(arr2))