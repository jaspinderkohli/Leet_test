class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = {}
        for i in range(len(s)-9):
            sub_seq = s[i:i+10]
            if sub_seq not in seq:
                seq[sub_seq] = 1
            else:
                seq[sub_seq] += 1
        res = []
        for k,v in seq.items():
            if v > 1:
                res.append(k)
        return res
