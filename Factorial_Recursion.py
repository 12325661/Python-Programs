def fact(n):
     if(n==1 or n==0):
            return 1
     else:
         return fact(n-1)*n
print("Factorial is:",fact(int(input("Enter the number:"))))
# fact(int(input("Enter the Number:")))