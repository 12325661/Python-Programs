# def converter(USD_val):
#     inr_value = USD_val * 83
#     print(USD_val,"USD =",inr_value,"INR")
# converter(int(input("Enter the $ :")))


def even(n):
    if n % 2 == 0:
        print("The Number is Even")
        return even
    else:
        print("Number is ODD")
even(int(input("Enter the number:")))