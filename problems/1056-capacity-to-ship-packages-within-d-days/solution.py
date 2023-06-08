class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            day = 1
            total = 0
            for weight in weights: 
                total += weight
                if total > capacity:
                    total = weight
                    day +=1
                    if day > days:
                        return False
            return True

        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l=mid + 1
        return l
