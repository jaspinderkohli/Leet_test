class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # print i
                nums[x]=nums[i]
                x+=1
        while x < len(nums):
            nums[x] = 0
            x+=1
        return x
        
