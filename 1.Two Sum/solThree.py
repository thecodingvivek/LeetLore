nums = [2,7,11,15]
target = 9

nums = [(v, i) for i, v in enumerate(nums)]
nums.sort()
fpointer = 0
lpointer = len(nums) - 1
sumo = 0


while fpointer < lpointer:
    sumo = nums[fpointer] + nums[lpointer]
    if sumo == target:
        print( [nums[fpointer][1],nums[lpointer][1]])
        break
    elif sumo < target:
        fpointer+=1
    else:
        lpointer -=1
    
    