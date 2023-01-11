def removeDuplicates(nums):
    i = 0
    j = 0
    length = 0 
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            length = i + 1
    return length 
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4,7,8]))