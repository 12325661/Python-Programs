n = int(input("Enter the number: "))
for i in range(1, n+1):
    
    # Printing spaces
    print(" " * (n - i), end="")
    # Printing stars
    print("*" * (2*i - 1))


