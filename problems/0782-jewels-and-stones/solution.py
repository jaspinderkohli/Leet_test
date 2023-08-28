class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for fin_char in stones:
            for char in jewels:
                if fin_char == char:
                    cnt+=1

        return cnt
