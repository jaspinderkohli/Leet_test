class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = (2 * n) * [None]
        for i,x in enumerate(nums):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
