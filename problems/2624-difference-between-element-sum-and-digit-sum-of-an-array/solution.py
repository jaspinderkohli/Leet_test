class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        dig = ''
        for i in nums:
            dig+=str(i)
        element_sum = sum(nums)
        dig_sum = 0
        for i in dig:
            dig_sum +=int(i)
        return abs(element_sum-dig_sum)
        
