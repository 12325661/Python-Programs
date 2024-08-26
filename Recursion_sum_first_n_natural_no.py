def calc_sum(n):
    if n == 0:  # Base case
        return 0
    else:
        return calc_sum(n-1) + n  # Recursive case

n = int(input("Enter the number: "))
print("Sum is:", calc_sum(n))
