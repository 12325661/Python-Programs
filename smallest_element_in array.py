def smallest_element(arr):
    arr.sort()
    return arr[-1]
arr1=[2,5,1,3,0]
arr2=[8,10,5,7,9]
print(smallest_element(arr1))
print(smallest_element(arr2))