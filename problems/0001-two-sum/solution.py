class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, x in enumerate(nums):
            if (target - x) not in dic:
                dic[x]= i
            else:
                return [i,dic[target - x]]
        print(dic)
       
