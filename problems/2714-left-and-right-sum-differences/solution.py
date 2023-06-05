class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans =  [0] * n
        left = [0] * n
        right = [0] * n
        for i,x in enumerate(nums):
            left[i] = sum(nums[:i])
            right[i] = sum(nums[i+1:])
            ans[i] =  abs(left[i] - right[i])
        return ans
    
