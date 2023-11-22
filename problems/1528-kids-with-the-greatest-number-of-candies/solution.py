class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = len(candies) * [None]
        max_candie = max(candies)
        for i, x in enumerate(candies):
            res[i] = (x + extraCandies >= max_candie)
        return res 

