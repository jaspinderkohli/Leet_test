class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = len(s) * [0]
        for i,x in enumerate(indices):
            new_s[x] = s[i]
        return ''.join(new_s)
