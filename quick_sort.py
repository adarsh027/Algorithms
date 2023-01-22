# Quicksort with in-place sorting
# Source: https://www.youtube.com/watch?v=COk73cpQbFQ&list=PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U&index=7
# https://www.youtube.com/watch?v=OTx0iWCClbg
#https://www.youtube.com/watch?v=zyoVdrFW6E8&t=136s
#1. partition logic 
# (i) Assume end element as pivot and partioning index(p_indx) at the start. This pivot needs to be 
# placed at the correct position(ie,partioning index)such that all elements smaller than the pivot are 
# to the left of pivot and all elements greater than pivot are to the right of pivot.
# (ii) Consider pivot swapped with element at p_indx position.Iterate through i =start to  end -1 and compare
# pivot at p_indx position with the position of ith element and check if it violates the partition rule of 
# having smaller elemets to left and larger elements to the right of pivot.
# Since we have assumed p_indx= start, the partition rule will be violated whenever ith element 
# is less than or equal to pivot,ie, arr[i] <= pivot.Whenever partition rule is violated, swap ith element, arr[i]
# and element at p_indx, arr[p_indx]. After swapping, increment p_indx as the current position of p_indx violated the 
# partition rule. The idea behind swapping and incrementing p_indx is to bring all elements less than or equal to pivot
# to the left of p_indx.You should always imagine the pivot element being swapped with element at p_indx whenever you are
# doing the comparison(ie, arr[i] <= pivot) to test the partition criteria.
# (iii) After all end-1 elemtns are iterated, p_indx has the correct value. Thus, we can swap the pivot which is at the end
# with the element at p_indx. Thus, the pivot is now sorted.Rememeber that throughout the iteration, the pivot was at its
# original position(which is at the end); we only imagined the pivot to be at p_indx.

# 2. repeat the same process recursively to sort the left portion of pivot . Base condition : len(arr) == 1
# 3. repeat the same process recursively to sort the right portion of pivot . Base condition : len(arr) == 1
# 4. After steps 1,2 and 3 are done, the whole array will become sorted. The steps 1,2 and 3 are carried out only if the
# criteria start<end is met.


def partition(arr, start, end):
    pivot = arr[end]     # pivot
    p_indx = start
    for i in range(start, end):
          if arr[i] <= pivot:
              print(arr[i], arr[p_indx] )
              arr[i], arr[p_indx] = arr[p_indx], arr[i]
              p_indx = p_indx + 1
              # print(arr,p_indx)
    arr[p_indx], arr[end] = arr[end], arr[p_indx]
    return p_indx

# Function to do Quick sort
def quickSort(arr, start, end):
#     if len(arr) <= 1:
#         return arr
    if start < end:
        pi = partition(arr, start, end)
        print("pi is: ", pi, arr)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)


arr = [11,24,43,7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)


#Quicksort using two pointers:left and right
#left keeps moving to the right as along as array[left] <= pivot
#right keeps moving to the left as along as array[right] > pivot
#ref: https://www.youtube.com/watch?v=zjzQVKqYr1U&list=PLzgPDYo_3xunyLTJlmoH8IAUvet4-Ka0y&index=7
#ref: https://www.youtube.com/watch?v=9KBwdDEwal8
#ref: https://www.youtube.com/watch?v=h8eyY7dIiN4
def partition(arr, start, end):
    pivot = arr[end]
    left = start
    right = end-1

    while True:
        while left <= right and arr[left] <= pivot:# use arr[left] >= pivot if you want to sort in descending order
            left = left + 1
        while left <= right and arr[right] >= pivot:# use arr[left] <= pivot if you want to sort in descending order
            right = right - 1
            print("left and right are: ", left,right)
        print("left and right are: ", left,right)
        if left<=right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
            
    # now as  left and right have crossed(ie,left>=right), we have found the correct 
    #value of partition index and hence, we can swap the pivot which is at the end with the element at left.
    arr[left], arr[end] = arr[end], arr[left]# 
    return left

# Function to do Quick sort
def quickSort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        print("pi is: ", pi, arr)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)


arr = [11,24,43,7, 8, 9, 1, 5,7]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)

#Quicksort without in-place sorting
#source : https://www.youtube.com/watch?v=kFeXwkgnQ9U&list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv&index=4

def quick_sort(arr):
    left_arr = []
    right_arr= []
    if len(arr)<=1:
        return arr
    else:
        pivot= arr.pop()
    for i in arr:
         if i>pivot:
             right_arr.append(i)
         else:
             left_arr.append(i)
            
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
print(quick_sort([13,7,2,45,1]))
