#logic
#1. Outer loop: move towards right from 1 to len(arr)-1
#(i) Consider the 1st element of the array at i=0 as sorted portion of array
# and the remaining as unsorted portion of array.
#(ii) consider 1st element of unsorted portion of array as current element whose
#  correct position we need to find and insert it there.
#(iii) Assume correct position for the current element j to be equal to 
# rightmost element of sorted portion,ie, one index less than the index of current element. Thus, the actual correct position for the current element
# will be at one position greater,ie, j+1, since all elements upto the element arr[j] is sorted.
#2. Inner loop :From the left of current, starting from j = i-1 upto j = 0, and as 
#long as the condition j>=0 and arr[j] > current is met, 
# shift each jth element to the right by one position
# and decrement j by 1.
#3. When the inner loop exits,j+1 will be the correct index 
# for the current element; thus we insert  the current element
# the (j+1) index.
#4. This process repeats in the the next iteration of outer loop and when the outer loop 
# finshes, the given array becomes a sorted array, completely.
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






