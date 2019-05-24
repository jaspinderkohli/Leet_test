class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        newdic = {}
        for x in range(0,len(nums)):
            if nums[x] in newdic:
                return [newdic[nums[x]], x]
            else:
                newdic[target - nums[x]] = x

        
