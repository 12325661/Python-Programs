marks= int(input("Enter the marks of the Student: "))
if(marks>=90):
 grade = "A"
elif(marks>=80 and marks<90):
 grade  =  "B"
elif(marks>=70 and marks<80):
 grade="C"
else:
 grade="D"
 print(" the grade of the Student ->",grade)