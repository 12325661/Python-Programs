# Rotate array by K elements : Block Swap Algorithm
# Helper function to swap two parts of the array
def swap(arr, start1, start2, size):
    for i in range(size):
        arr[start1 + i], arr[start2 + i] = arr[start2 + i], arr[start1 + i]

# Function to perform block swap algorithm for array rotation
def block_swap(arr, k, n):
    # If k is 0 or k equals the array size, no need to rotate
    if k == 0 or k == n:
        return arr
    
    # A recursive helper function to perform block swaps
    def rotate_recursive(arr, start, k, n):
        # Base case
        if k == 0 or k == n:
            return

        if k < n - k:  # Case 1: k < n - k
            swap(arr, start, start + n - k, k)
            rotate_recursive(arr, start, k, n - k)
        elif k > n - k:  # Case 2: k > n - k
            swap(arr, start, start + k, n - k)
            rotate_recursive(arr, start + n - k, k - (n - k), k)
        else:  # Case 3: k == n - k
            swap(arr, start, start + k, k)

    # Initial call to the recursive rotation
    rotate_recursive(arr, 0, k, n)
    return arr

# Test case
arr1 = [1, 2, 3, 4, 5]
k1 = 2
n1 = len(arr1)

arr2 = [1, 2, 3, 4, 5, 6, 7]
k2 = 3
n2 = len(arr2)

# Rotate and print the results
print("Rotated array (k=2):", block_swap(arr1, k1, n1))  # Output: [3, 4, 5, 1, 2]
print("Rotated array (k=3):", block_swap(arr2, k2, n2))  # Output: [4, 5, 6, 7, 1, 2, 3]


##******************************************************************************

def rotate_array(arr, k):
    n = len(arr)
    # Adjust k in case it's larger than the array size
    k = k % n
    
    # Rotate the array by slicing and concatenating
    return arr[k:] + arr[:k]

# Test cases
arr1 = [1, 2, 3, 4, 5]
k1 = 2
print("Rotated array1:", rotate_array(arr1, k1)) 
arr2 = [1, 2, 3, 4, 5, 6, 7]
k2 = 3
print("Rotated array2:", rotate_array(arr2, k2))  
