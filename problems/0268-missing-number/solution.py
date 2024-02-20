class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        i = 0
        # for i in range(0, n+1):
        #     # mid = l
        #     if i not in nums:
        #         return i
        print("len : ", n)
        print("sorted", nums)
        while i < n:
            mid = (i + n) // 2
            if mid == nums[mid]:
                i = mid + 1
            else:
                n = mid
                
        return i
