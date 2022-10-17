class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j =0, 0
        cnt = []
        while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    cnt.append(s[i])
                    i+=1
                    j+=1
                else:
                    j+=1
        if ''.join(cnt) == s:
            return True
        return False
