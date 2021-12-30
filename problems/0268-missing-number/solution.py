class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = r = 0
        
        for i in range(0, n+1):
            if i not in nums:
                return i
