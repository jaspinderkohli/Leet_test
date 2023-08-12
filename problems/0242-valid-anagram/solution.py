class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_an = sorted(s)
        t_an = sorted(t)
        return s_an == t_an
