class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # nums.sort()
        # # nums = set(nums)
        # print(nums)
        # cnt=1
        # bigct = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1]:
        #         if nums[i] == nums[i-1] +1:
        #             cnt+=1
        #         else:
        #             bigct = max(bigct,cnt)
        #             cnt=1
        # return max(bigct,cnt)
        
        long_str = 0
        nums_set = set(nums)
        
        print(nums_set)
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in nums_set:
                    current_num +=1
                    current_streak +=1
                long_str = max(long_str, current_streak)
        return long_str
