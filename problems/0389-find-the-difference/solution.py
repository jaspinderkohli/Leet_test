class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for _word in s:
            t = t.replace(_word,'', 1)
        return t
