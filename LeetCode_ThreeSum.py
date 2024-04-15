def threeSum(nums):
    nums.sort()
    length = len(nums)
    mySet = set(())
    # result = list(())
    for i in range(length):
        j = i + 1
        k = length -1
        while j < k :
            sum = nums[i]+ nums[j] + nums [k]
            if sum == 0:
                mySet.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif sum > 0:
                k -= 1
            else :
                j += 1
    
    result = list(mySet)
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
