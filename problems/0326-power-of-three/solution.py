class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n  == 1:
            return True
        elif n == 0:
            return False
        else:
            return n % 3 == 0 and self.isPowerOfThree(n // 3)
        '''
            We say that for a number, lets call it n, to be a power of 3 it must be divisible by 3 and the result of dividing n by 3 must also be divisible by 3 and so on and so forth
        '''
