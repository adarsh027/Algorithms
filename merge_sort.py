#Ref: https://www.youtube.com/watch?v=nCNfu_zNhyI
# https://www.youtube.com/watch?v=cVZMah9kEjI
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)
       
    # merge two sorted lists
    i = j = k = 0  #initialize i, j and k  for left, right and arr
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i+=1
        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1

    while i < len(left_arr):#this makes sure any remaining elements of left array are included in the merged array
        arr[k] = left_arr[i]
        i+=1
        k+=1

    while j < len(right_arr):#this makes sure any remaining elements of right array are included in the merged array
        arr[k] = right_arr[j]
        j+=1
        k+=1
        
    return arr

merge_sort([23,44,3,9,4,1,3,8])





