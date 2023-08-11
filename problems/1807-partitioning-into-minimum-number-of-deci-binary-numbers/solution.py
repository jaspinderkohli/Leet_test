class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        for char in n:
            digit = int(char)
            max_digit = max(max_digit, digit)
        return max_digit
