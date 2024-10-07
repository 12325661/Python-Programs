# def avg_array(arr):
#     total_sum = 0
#     # Step 1: Calculate the sum of the array elements
#     for num in arr:
#         total_sum += num
#     # Step 2: Calculate the number of elements in the array
#     n = len(arr)
#     # Step 3: Calculate the average
#     average = total_sum / n
#     # Step 4: Return integer average if it's a whole number, else return as float
#     if average.is_integer():
#         return int(average)
#     else:
#         return average

# # Test the function with example
# arr1 = [1, 2, 3, 4, 5]
# print("The average of the array:", avg_array(arr1))  # Output: 3
 
arr = [1, 2, 3, 4, 5]
average = sum(arr) / len(arr)  # Use len(arr) to ensure it works for any array size

# Check if the average is a whole number
if average.is_integer():
    average = int(average)  # Convert to integer if it's a whole number

print(average)  # Print the result

