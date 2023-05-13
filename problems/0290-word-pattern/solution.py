class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        pat_s = {}
        s_pat = {}

        for i, x in enumerate(pattern):
            if x not in pat_s:
                pat_s[x] = words[i]
            elif pat_s[x] != words[i]:
                return False

            if words[i] not in s_pat:
                s_pat[words[i]] = x
            elif s_pat[words[i]] != x:
                return False

        return True
