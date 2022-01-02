class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # for i in range(m, len(nums1)):
        i = m
        while i < len(nums1):
            # print(i, nums1[i])
            for j in range(0,n):
                nums1[i] = nums2[j]
                i+=1
        nums1.sort()
        
