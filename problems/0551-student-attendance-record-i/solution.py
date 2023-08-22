class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_A = 0
        cnt_L = 0

        for i,x in enumerate(s):
            if x == 'A':
                cnt_A+=1
            if (i >=2) and (s[i-1] == 'L' and s[i-2] == 'L' and s[i] == 'L'):
                return False
        
        if cnt_A >= 2:
            return False
        return True
