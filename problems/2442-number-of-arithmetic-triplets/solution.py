class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        cnt=0
        for i in range(0,n):
            for j in range(i,n):
                for k in range(j,n):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        cnt +=1
        return cnt


