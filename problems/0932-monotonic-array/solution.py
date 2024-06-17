class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increaing = True
        is_decreasing = True

        for i in range(1 ,len(nums)):
            # check if increasing
            if nums[i] < nums[i-1]:
                is_increaing = False
            # check if decreasing
            if nums[i] > nums[i-1]:
                is_decreasing = False
        return is_increaing or is_decreasing
