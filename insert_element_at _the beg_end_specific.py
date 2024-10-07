def insert_at_begning(arr,element):
    arr.insert(0,element)
def insert_at_end(arr,element):
    arr.append(element)
def insert_at_position(arr,element,pos):
    arr.insert(pos-1,element)
    n=5
arr=[1,2,3,4,5]
insert_at_begning(arr,6)
insert_at_end(arr,7)
insert_at_position(arr,8,4)
print("modified array:",arr)#Output: 6,1,2,8,3,4,5,7