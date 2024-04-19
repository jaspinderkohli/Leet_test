class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i,x in enumerate(nums):
            if target - x in dic.keys():
                return [i, dic[target-x]]
            dic[x] = i

        '''
            nums = [2,7,11,15]

            target - x ==> 9 - 7 == 2
            dic = {
                2 : 0
                7 : 1
            }

        '''
