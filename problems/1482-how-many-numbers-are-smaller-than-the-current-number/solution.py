class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsCopy = list(nums)
        numsCopy.sort()
        dic = {
            
        }
        for i,x in enumerate(numsCopy):
            if x not in dic:
                dic[x] = i
        res = []
        for i in nums:
            res.append(dic[i])
        return res
