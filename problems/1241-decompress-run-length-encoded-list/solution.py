class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        new = []
        while i < len(nums):
            freq = nums[i]
            val = nums[i+1]
            things_to_add = freq*[val]
            _ = [new.append(x) for x in things_to_add]
            i+=2
        return new


