n = int(input("Enter the number: "))

for i in range(n):
    # Printing spaces for alignment
    print(" " * (n - i - 1), end="")
    
    num = 1  # Initialize num for each row
    for j in range(i + 1):
        print(num, end=" ")  # Print the number with a space
        num = num * (i - j) // (j + 1)  # Calculate the next number in the row

    print()  # Move to the next line after each row
