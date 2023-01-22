#selection sort logic(finding minimum and swapping)
# 1. Find minimum of unsorted part of arr.
# 2. Within the array, swap the minimum value with the current element.
#note: You should swap with the minimum index element not the minimum variable "min" so that swap happens within the array. If
# you swap with the minimum value, you are not actually swapping the elements within the array, you are just swapping the values of current element and the minimum variable.
# 3. repeat steps 1 and 2 for len(arr) times to sort all the elemets of arr.Note: If 
# you have sorted upto n-1 elements of an array, either from right or from left, the array is already sorted. Thus,
# you can further optimize it minutely by repeating step 1 for n-1 = len(arr)-1 times instead of repeating
# it for n times. This point is also mentioned in anuj bhaiya's selection sort youtube video).
#Ref: https://www.youtube.com/watch?v=B-nqY6IYqVw&t=106s
def selection_sort(arr):
    for i in range(len(arr)):
            #find minimum of unsorted part of arr
            min= arr[i]
            min_indx=i
            for j in range(i+1,len(arr)):
                if arr[j]<min:
                    min= arr[j]
                    min_indx=j
            print("minimum of unsorted part of arr after {}th iteration: {}".format(i,min))
            #swap
            arr[i],arr[min_indx]=arr[min_indx],arr[i]
            
    return arr
print(selection_sort([567,3,12,45,2,13,7,2,45,1]))


#to find minimum value in an array logic
#Assume 1st element to be minimum
#Comapre each element of the remainig elements with minimum and update minimum
def find_min(arr):
    min= arr[0]
    min_indx = 0
    for i in range(1,len(arr)):
        
        if arr[i]<min:
            min= arr[i]
            min_indx=i
    return min,min_indx

find_min([123,4,1,56,13,7,2,45,16])