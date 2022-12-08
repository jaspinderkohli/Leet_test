class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # Initialize the sum and count to 0
        sum = 0
        cnt = 0
        for x in nums:
            if x % 2 == 0 and x % 3 == 0:
                sum+=x
                cnt+=1
                
        # Return the average value
        if cnt > 0:
            return int(sum/cnt)
        return 0
