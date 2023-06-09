class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed) -> bool:
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/speed)
                if total_hours > h:
                    total_hours = pile
                    return False
            return True

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

