# tup = (1)       # This is just an integer, not a tuple.
# print(tup)     # This assigns the integer 1 to the variable 'print'.
# print(type(tup))  # This will cause an error because 'print' is now an integer, not a function.
tup = (1, 2, 3, 4,1)

# Slicing the tuple to get elements from index 1 to 2 (3 is not included)
print(tup[1:3])        # Output: (2, 3)

# Checking the type of the tuple
print(type(tup))  # Output: <class 'tuple'>

# Finding the index of the element '3' in the tuple
print(tup.index(4))    # Output: 2
print(tup.count(1))# it will return the occurence of the index$
