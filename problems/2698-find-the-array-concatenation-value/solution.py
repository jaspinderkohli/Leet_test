class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        conc = 0
        n = len(nums)

        if n < 2:
            return nums[0]
        
        while len(nums) > 1:
            number = str(nums[0]) + str(nums[-1])
            conc += int(number)
            nums.pop()
            nums.pop(0)
        
        if nums:
            conc +=nums[0]

        return conc
