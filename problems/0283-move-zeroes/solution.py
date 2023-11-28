class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        while l < len(nums) - 1:
            if nums[l] == 0:
                if r >= len(nums):
                    break
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    r +=1
                else:
                    r +=1
                    continue
            l+=1
            r = max(r, l+1)
        return nums
