nums = [1,3,2,3,1]

#[1,2,3] 
#[1,3]

count=[0]
def getPair(fhalf,rhalf):
    j=0
    for i in range(len(fhalf)):
        while j < len(rhalf) and rhalf[j]*2 < fhalf[i]:
                j+=1
        count[0]+=j



def merge(fhalf,shalf):
    getPair(fhalf,shalf)
    i = 0
    j= 0
    arr=[]
    while i<len(fhalf) and j<len(shalf):
        if fhalf[i] < shalf[j]:
            arr.append(fhalf[i])
            i+=1
        else:
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

mergeSort(nums)
print(count)