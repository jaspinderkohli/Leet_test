class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0 , n -1 
        result = [0] * n
        pos = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[pos] = nums[l] ** 2
                l+=1
            else:
                result[pos] = nums[r] ** 2
                r-=1
            pos-=1
        return result
