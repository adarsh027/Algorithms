#Ref: https://www.youtube.com/watch?v=nCNfu_zNhyI
# https://www.youtube.com/watch?v=cVZMah9kEjI
def merge_sort(arr):
    if len(arr) <= 1:
        return
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    merge_sort(left_arr)
    merge_sort(right_arr)
    merge_two_sorted_lists(left_arr, right_arr, arr)   
    return arr
    
def merge_two_sorted_lists(left,right,arr):
    #initialize i, j and k  for left, right and arr
    i = j = k = 0 
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while i < len(left):#this makes sure any remaining elements of left array are included in the merged array
        arr[k] = left[i]
        i+=1
        k+=1

    while j < len(right):#this makes sure any remaining elements of right array are included in the merged array
        arr[k] = right[j]
        j+=1
        k+=1

merge_sort([23,44,3,9,4,1,3,8])





