def print_list(list, idx):
    if idx == len(list):  # Base case: when the index reaches the end of the list
        return
    print(list[idx])  # Print the current element
    print_list(list, idx + 1)  # Recursively call the function with the next index

fruits = ["Mango", "Litchi", "Orange", "Apple"]
print_list(fruits, 0)
