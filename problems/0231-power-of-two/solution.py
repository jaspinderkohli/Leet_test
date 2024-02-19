class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while i < n:
            if 2 ** i == n:
                return True
            elif 2 ** i < n:
                i+=1
            elif 2 ** i > n:
                return False
        
