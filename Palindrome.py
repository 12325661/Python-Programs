# Function to check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Define the range
n=int(input())
m=int(input())

# Find palindrome numbers in the range and count them
count_palindromes = 0
for num in range(n, m+1):
    if is_palindrome(num):
        count_palindromes += 1

# Print the count of palindrome numbers
print(count_palindromes)
