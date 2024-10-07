# binary_number = "1100110"
# # First convert binary to decimal
# decimal_number = int(binary_number, 2)
# # Then convert decimal to octal
# octal_number = oct(decimal_number)[2:]  # [2:] to remove '0o' prefix
# print(octal_number)
decimal = 15
binary = bin(decimal)[2:]  # [2:] removes the '0b' prefix
print(binary)
