# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 1
        high = n
        while i <= high:
            mid = (i + high) //2
            if guess(mid) == -1 :
                high = mid -1
            elif guess(mid) == 1:
                i = mid + 1
            elif guess(mid) == 0:
                return mid
        return i
            
