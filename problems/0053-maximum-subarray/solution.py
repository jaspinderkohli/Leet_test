class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_arr = curr_arr = nums[0]
        for i in range(1,len(nums)):
            curr_arr = max(nums[i], curr_arr+nums[i])
            if curr_arr > best_arr:
                best_arr = curr_arr
        return best_arr
