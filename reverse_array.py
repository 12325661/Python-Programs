def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    
    return reversed_arr
arr1 = [5, 4, 3, 2, 1]
arr2 = [10, 20, 30, 40]
print("Reversed array:", reverse_array(arr1))  
print("Reversed array:", reverse_array(arr2))  