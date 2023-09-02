class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maximun, minimum = 0, 0
        max_el = max(nums)
        min_el = min(nums)
        max_el_idx = nums.index(max_el)
        min_el_idx = nums.index(min_el)

        big_idx = max(max_el_idx, min_el_idx)
        small_idx = min(max_el_idx, min_el_idx)

        return min(big_idx + 1, len(nums) - small_idx, small_idx + len(nums)- big_idx + 1)
