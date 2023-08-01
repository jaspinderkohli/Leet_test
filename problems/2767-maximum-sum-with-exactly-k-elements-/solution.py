class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        tot_sum = 0
        i=0
        num = max(nums)
        while i < k:
            tot_sum = tot_sum + num
            num +=1 
            i+=1
        return tot_sum

