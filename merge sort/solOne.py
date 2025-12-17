nums = [2,3,1,5,7,4,9]

def merge(fhalf,shalf):
    print(fhalf,shalf)
    i = 0
    j= 0
    arr=[]
    while i<len(fhalf) and j<len(shalf):
        if fhalf[i] < shalf[j]:
            arr.append(fhalf[i])
            i+=1
        elif shalf[j] < fhalf[i]:
            arr.append(shalf[j])
            j+=1
    

    while i<len(fhalf):
        arr.append(fhalf[i])
        i+=1
    
    while j<len(shalf):
        arr.append(shalf[j])
        j+=1
    
    return arr

def mergeSort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    fhalf = mergeSort(nums[:mid])
    shalf = mergeSort(nums[mid:])
    return merge(fhalf,shalf)

print(mergeSort(nums))

