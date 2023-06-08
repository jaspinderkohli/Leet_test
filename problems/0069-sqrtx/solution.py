class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(sqrt(x))
        '''
            8
            2 ** 2
            3 ** 3
            
            First we need to search for minimal k satisfying condition k^2 > x, 
            then k - 1 is the answer to the question. We can easily come up with the solution. Notice that I set right = x + 1 instead of right = x to deal with special input cases like x = 0 and x = 1.
        '''
        l, r = 0 , x+1
        while l < r:
            mid = (l+r) // 2
            if mid * mid > x:
                r = mid
            else:
                l = mid + 1
        return l-1


