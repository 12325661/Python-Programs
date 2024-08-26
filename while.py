nums = (1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number:"))
i=0
while i<len(nums):
    if nums[i]==x:
        print("The number is present in the tuple",i)
        i+=1
        break
    else:
        print("The number is not founded")
        break
        