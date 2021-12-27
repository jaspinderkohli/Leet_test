# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        high = n
        while(i < high):
            mid = (i+high) // 2
            if (isBadVersion(mid)):
                high = mid
            else:
                i = mid + 1
        return i
