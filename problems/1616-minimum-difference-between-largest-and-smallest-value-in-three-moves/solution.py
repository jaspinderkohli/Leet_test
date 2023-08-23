class Solution:
    def minDifference(self, nums: List[int]) -> int:
        [1,5,0,10,14]

        '''
            [1,5,0,10,14]

            1st move

            [1,0,0,10,14]

            2nd move

            [1,0,0,0,14]

            3rd move

            [1,0,0,0,0]

            1

        '''

        
        
        if len(nums) <= 4:
            return 0
        
        nums.sort()

        min_dif = float('inf')
        #  dif of 3 largest and 3 smallest
        for i in range(4):
            min_dif = min(min_dif, nums[-4+i]- nums[i])
        return min_dif



