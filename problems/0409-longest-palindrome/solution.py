class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
            first check how many char are odd and even
        '''
        odd_cnt = 0
        d = {}

        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                odd_cnt +=1
            else:
                odd_cnt -=1
        if odd_cnt > 1:
            return len(s) - odd_cnt + 1
        return len(s)
