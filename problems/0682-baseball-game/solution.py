class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_l = []
        for x in operations:
            try:
                if type(int(x)) == int:
                    new_l.append(int(x))
            except:
                pass
            if x == '+':
                new = new_l[-1] + new_l[-2]
                new_l.append(new)
            elif x == 'D':
                new = new_l[-1] * 2
                new_l.append(new)
            elif x == 'C':
                new_l.pop()
        return sum(new_l)
