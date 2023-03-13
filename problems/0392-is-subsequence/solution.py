class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
            compare both strings s and t and add common characters to a list
            then compare that list
        '''

        i = j = 0
        lis = []
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                lis.append(s[i])
                i+=1
                j+=1
            else:
                j+=1
        return ''.join(lis) == s
