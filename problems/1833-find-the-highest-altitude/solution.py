class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = float('-inf')
        cnt = 0
        for num in gain:
            cnt+=num
            max_alt = max(max_alt, cnt)
        return max_alt if max_alt > 0 else 0
