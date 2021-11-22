class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = bal = 0
        for  x in s:
            if x == 'L':
                bal+=1
            else:
                bal-=1
            if not bal:
                out+=1
        return out
            
