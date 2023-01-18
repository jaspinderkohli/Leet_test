class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        target = num
        l = 1
        h = target
        while (l <= h):
            mid = (l+h) // 2
            if (mid ** 2) > target:
                h = mid - 1
            elif (mid ** 2) < target:
                l = mid + 1
            elif (mid ** 2) == target:
                return True
        return False
