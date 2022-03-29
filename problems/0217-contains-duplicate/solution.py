class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
            [1,2,3,1]
        """
        distinct_nums = set(nums)
        return len(nums) != len(distinct_nums)
        
