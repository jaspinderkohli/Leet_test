class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        # return nums
        return nums[::-1][k-1]
