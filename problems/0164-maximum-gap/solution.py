class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # if list contains only 1 element return 0
        if len(nums) < 2:
            return 0

        # sort the list
        nums.sort()
        max_diff = 0  #initialize the max diff to 0
        
        for i in range(0, len(nums)-1):
            curr_diff =  nums[i+1] - nums[i]
            if curr_diff > max_diff:
                max_diff = curr_diff
        return max_diff

