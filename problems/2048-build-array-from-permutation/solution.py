class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = len(nums)* [None]
        for i,x in enumerate(nums):
            ans[i] = nums[nums[i]]
        return ans
