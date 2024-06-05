class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        '''
        Example 1

            s = "co aching"
            t = "co ding"

            add "ding"
        
        '''

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i+=1
                j+=1
            else:
                i+=1
        return len(t[j:])
