
n = int(input("Enter the number: "))

# Upper part of the diamond
for i in range(1, n + 1):
    # Printing spaces
    print(" " * (n - i), end="")
    # Printing stars
    print("*" * (2 * i - 1))

# Lower part of the diamond
for i in range(n - 1, 0, -1):
    # Printing spaces
    print(" " * (n - i), end="")
    # Printing stars
    print("*" * (2 * i - 1))
