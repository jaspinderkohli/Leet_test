class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i,x in enumerate(nums):
            if x != val:
                nums[index] = x
                index+=1
        return index
