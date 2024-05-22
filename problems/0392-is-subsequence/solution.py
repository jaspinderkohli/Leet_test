class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
            Example 1 
                s = 'abc'
                t = 'ahbgdc'

                idx == ??
                

        '''
        i = j = 0
        con = ''
        
        if not s:
            return True

        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                con+=t[j]
                j+=1
                i+=1
            else:
                j+=1
        return s == con

