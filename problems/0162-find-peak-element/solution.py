class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        '''
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r) // 2 
            if nums[mid] > nums[mid+1]:
                '''
                    If the middle element is greater than the next element,
                    it means a decreasing slope is encountered. The peak
                    element is either at mid or on the left side of mid.
                '''
                r = mid
            else:
                '''
                    If the middle element is less than or equal to the next element,
                    it means an increasing slope is encountered. The peak element
                    is on the right side of mid.
                '''
                l = mid + 1
        return l
            



