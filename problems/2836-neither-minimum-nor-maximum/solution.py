class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        max_num, min_num = nums[0], nums[0]
        for num in nums:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        # print('max', max_num,  'min->', min_num)
        for num in nums:
            if num not in [max_num, min_num]:
                return num
