#bubble sort logic(adjacent pair comparison and swapping)
# 1 Compare every adjacent pairs of arr and swap.(Note: For an unsorted array of 
# size n = len(arr),there will be n-1 = len(arr)-1 comparisons). After each pass of adjacent pair swapping, 
# the largest among unsorted part of arr is moved to the right and thus becomes sorted. 
# Thus, to sort n elements, would required n such passes.

# 2 Repeat step 1 for n= len(arr) times so that all the n elements of arr are sorted. (Note: If 
# you have sorted upto n-1 elements of an array, either from right or from left, the array is already sorted. Thus,
# you can further optimize it minutely by repeating step 1 for n-1 = len(arr)-1 times instead of repeating
# it for n times. This point is also mentioned in anuj bhaiya's selection sort youtube video).

def bubble_sort(arr):
    for i in range(len(arr)):
            for j in range(0,len(arr)-1):
                print(arr[j],arr[j+1])
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)

    return arr
            
bubble_sort([13,7,2,45,1])

#optimized version of bubble sort
def bubble_sort(arr):
    #count=0
    for i in range(len(arr)-1):
            swapped= False
            #count+=1
            for j in range(0,len(arr)-1 - i):# subtracting i ensures we consider only the unsorted part of arr in each pass
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped=True
            if swapped==False:# If no swapping occured then the array is already sorted, and you can exit the outer loop.This condition ensures that we don't make redundant passes, especially in situations when the array becomes sorted at an early stage(ie, within a few initial passes) or the given array is already sorted.
                break
    
    return arr
            
bubble_sort([1,2,3,4,5])


# while loop version of bubble sort
def bubble_sort(arr):
    swapped = True
    count=0
    while swapped:
        swapped = False
        count=count+1
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped=True
    return arr,count


bubble_sort([13,7,2,45,1])



