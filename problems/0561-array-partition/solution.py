class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        odSum = 0
        for i in range(0,len(nums),2):
            odSum += nums[i]
        return odSum
