list1 = [1,2,3,2,1]
# list2 = [1,2,3,4,5]
copy_list=list1.copy()
copy_list.reverse()
if(copy_list==list1):
    print("list is palindrome ")
else:
    print("list is not palindrome ")