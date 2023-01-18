class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans_arr = []
        nums1 = list(set(nums1))
        
        for i in nums1:
            if i in nums2:
                ans_arr.append(i)
        return ans_arr

