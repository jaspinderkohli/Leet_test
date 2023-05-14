import math
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        '''
            1. 3 highest 
            2. 2 lowest 1 highest
            compare results
        '''
        nums.sort()

        last = nums[-1]
        highest_3 = nums[-3:]

        case_2_prod = math.prod(highest_3)
        if min(nums)<0:
            lowest_2 = nums[0:2]
            case_1_prod = last * math.prod(lowest_2)
            return max(case_1_prod,case_2_prod)
        return case_2_prod


        
