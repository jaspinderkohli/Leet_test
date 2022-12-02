class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
            case 1 - 
                    < 0 and > n ale kadh lo
            case 2 -
                    je ehna ch ni fer it must be n+1 
        '''
        n = len(nums)
        for i in range(0,n):
            if nums[i] <= 0:
                nums[i] = 0
        
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val-1] >0:
                    nums[val-1] *=-1
                elif nums[val-1] == 0:
                    nums[val-1] =-1* (n+1)
        for i in range(1,n+1):
            if nums[i - 1] >= 0:
                return i
        return n+1
        #     if nums[i] <= 0 or nums[i] > n:
        #         nums[i] = n + 1

        # for i in range(n):
        #     if 
        
        # for i in range(0, n):
        #     if nums[i] > 0 and nums[i] < n:
        #         pass
            

        



        # print('legth before ', len(nums))
        # nums.sort()
        # print('legth after ', len(nums))
        # nums = set(nums).copy()
        # print('legth after set ', len(nums))
        # max_num = max(set(nums))
        # i = 1
        # if max_num < 0:
        #     return 1
        # while i <= max_num + 1:
        #     if i not in nums:
        #         return i 
        #     i+=1
