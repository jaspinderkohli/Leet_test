class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(sqrt(x))
        '''
            8
            2 ** 2
            3 ** 3
        '''
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            l = 1 
            h = x
            while (l <= h):
                mid = (h + l) // 2
                if ( mid ** 2 <= x < (mid+1)**2):
                    return mid
                elif (mid ** 2 > x):
                    h = mid -1
                else:
                    l = mid + 1
