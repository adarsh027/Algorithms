#logic
#1. Outer loop(left to right, starting from i = 1 )
#(i) Consider the 1st element of the array at i=0 as sorted portion of array
# and the remaining as unsorted portion of array. We need to take each element 
# from the unsorted portion as current element and place it correctly within the sorted portion.
#(ii) Initialize j to be equal to be rightmost element of sorted portion,ie, one index less than the index of current element. 
#2. Inner loop(right to left, starting from j = i-1) : Shift elements from the sorted portion to the right as long as it is greater than the current element.
#3. When the inner loop exits,j+1 will be the correct index for the current element; thus we insert  the current element
# the (j+1) index.
#4. When the outer loop finshes, the given array becomes a sorted array, completely.
#Ref : https://www.enjoyalgorithms.com/blog/introduction-to-sorting-bubble-sort-selection-sort-and-insertion-sort/
# ref :https://www.youtube.com/watch?v=nKzEJWbkPbQ (Programming with Mosh)
def insertion_sort(arr):
    for i in range(1,len(arr)):
        current= arr[i]
        j= i-1 
        while j>=0 and arr[j] > current:
            j=j-1
        arr[j+1]=current 
    
    return arr
        
insertion_sort([3,7,2,45,1])


#using only for loops
def insertion_sort(arr):
    for i in range(1,len(arr)):
            current= arr[i]
            j=i-1
            for j in range(j,-1,-1):
                if arr[j]>current:
                   arr[j+1]=arr[j]
                   j=j-1
                else:
                     break
            arr[j+1]=current
                 
    return arr

insertion_sort([13,7,2,45,1])






