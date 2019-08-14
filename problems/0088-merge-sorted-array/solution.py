class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # print nums1
        # print m
        # print nums2
        # print n
        x = 0
        for i in range(m):
                nums1[x]=nums1[i]
                x+=1
        for j in range(len(nums2)):
            nums1[x]=nums2[j]
            x+=1
        return nums1.sort()
        
