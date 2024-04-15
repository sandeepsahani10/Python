def twoSum_again(nums, target):
    length = len(nums)
    dict={}
    for i in range(length) :
        comp = target - nums[i]
        if comp in dict.keys():
            return [i, dict[comp]]
        else:
            dict[nums[i]]=i
    return []
