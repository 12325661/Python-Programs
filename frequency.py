 def count_frequency(arr):
    # Initialize an empty dictionary to store the frequency of each element
    frequency = {}

    # Iterate through the array
    for num in arr:
        if num in frequency:
            frequency[num] += 1  # Increment count if element is already in the dictionary
        else:
            frequency[num] = 1  # Initialize count if element is not in the dictionary

    # Print the frequency of each element
    for num, count in frequency.items():
        print(num, count)

# Test arrays
arr1 = [10, 5, 10, 15, 10, 5]
print("The frequency of arr1 elements:")
count_frequency(arr1)

arr2 = [2, 2, 3, 4, 4, 2]
print("\nThe frequency of arr2 elements:")
count_frequency(arr2)
