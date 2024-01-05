class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i,x in enumerate(nums):
            if x != val:
                nums[idx] = x
                idx+=1
        return idx
