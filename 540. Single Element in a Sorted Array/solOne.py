nums =  [1,1,2,2,3,3,4,4,8,8,9]
#       [0,1,2,3,4,5,6,7,8,9,10] 

start = 0
end = len(nums) - 1

while start < end:
    mid = (start + end) // 2

    if mid % 2 == 1:
        mid -= 1
    
    if nums[mid] == nums[mid]+1:
        start = mid + 2
    else:
        end = mid

print()
