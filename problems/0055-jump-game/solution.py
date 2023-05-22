class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
            [2,3,1,1,4]
        '''
        last = len(nums)
        max_reach = 0
        for i in range(last):
            print(i, nums[i])
            if i > max_reach:
                return False
            # else:
            max_reach = max(max_reach, i + nums[i])
        
        return max_reach >= len(nums)-1
            
