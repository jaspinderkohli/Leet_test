class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        for i, x in enumerate(candies):
            out.append(x + extraCandies >= max(candies))
        return out

