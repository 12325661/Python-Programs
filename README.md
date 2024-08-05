# Python-Programs
num = int(input("Enter the number: "))
i = 2
f = 0

while i <= num // 2:
    if num % i == 0:
        f = 1
        break
    i += 1

if f == 1:
    print("Not a prime number")
else:
    print("Is a prime number")
