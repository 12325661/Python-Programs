i = int(input("Enter the number:"))
while i<=10:
    # if(i%2==0):
    if(i%2!=0):
        i+=1
        continue# skip
    print(i)
    i+=1