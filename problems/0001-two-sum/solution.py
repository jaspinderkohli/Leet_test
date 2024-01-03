class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dic = {}
        for i, x in enumerate(nums):
            if target - x in num_dic.keys():
                return [i , num_dic[target - x]]
            num_dic[x] = i
