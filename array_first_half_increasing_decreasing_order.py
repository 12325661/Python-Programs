def increasing_decreasing(arr):
    arr.sort()
    n=len(arr)
    mid=n//2
    first_half_arr=arr[:mid]
    second_half_arr = arr[mid:][::-1]
    return  first_half_arr+second_half_arr
arr1=[8,7,1,6,5,9]
print("Arranged array:",increasing_decreasing(arr1))
arr2=[4,2,8,6,15,5,9,20]
print("Arranged array:",increasing_decreasing(arr2))
