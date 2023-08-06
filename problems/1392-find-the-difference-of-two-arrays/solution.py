class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        l1 = [x for x in nums1 if x not in nums2]
        l2 = [x for x in nums2 if x not in nums1]
        return [l1,l2]
