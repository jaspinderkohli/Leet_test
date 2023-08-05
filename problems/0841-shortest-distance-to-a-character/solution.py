class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s = [x for x in s]
        pos_c = []
        for i,x in enumerate(s):
            if x == c:
                s[i] = 0
                pos_c.append(i)
        for i,x in enumerate(s):
            min_d = float('inf')
            for j in range(0, len(pos_c)):
                if x != 0:
                    min_d = min(abs(i-pos_c[j]),min_d)
                    s[i] = min_d
        return s
        # print(pos_c)
        # return s

