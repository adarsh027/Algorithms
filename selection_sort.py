#selection sort logic(finding minimum and swapping)
# 1 find minimum of unsorted part of arr.
# 2 swap the minimum with the current element.
# 3 repeat steps 1 and 2 for len(arr) times to sort all the elemets of arr.(Note: If 
# you have sorted upto n-1 elements of an array, either from right or from left, the array is already sorted. Thus,
# you can further optimize it minutely by repeating step 1 for n-1 = len(arr)-1 times instead of repeating
# it for n times. This point is also mentioned in anuj bhaiya's selection sort youtube video).
def selection_sort(arr):
    for i in range(len(arr)):
            #find minimum of unsorted part of arr
            min= arr[i]
            for j in range(i+1,len(arr)):
                if arr[j]<min:
                    min= arr[j]
                    min_indx=j
            print("minimum of unsorted part of arr after {}th iteration: {}".format(i,min))
            
            #swap
            arr[i],arr[min_indx]=arr[min_indx],arr[i]
                  
    return min, arr
print(selection_sort([13,7,2,45,1]))


#to find minimum value in an array logic
#Assume 1st element to be minimum
#Comapre each element of the remainig elements with minimum and update minimum
def find_min(arr):
    min= arr[0]
    for i in range(1,len(arr)):
        
        if arr[i]<min:
            min= arr[i]
            min_indx=i
    return min,min_indx

find_min([13,7,2,45,1])