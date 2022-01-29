class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for x in nums:
            if x not in dup:
                dup[x] = 1
            else:
                return True
        return False
