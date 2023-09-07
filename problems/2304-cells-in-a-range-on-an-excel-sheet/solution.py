class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        # print("Yo")
        start, end = s.split(":")
        print(start, end)
        # print(ord(start[0]))
        # print(chr(75))
        res = []
        for col in range(ord(start[0]), ord(end[0])+1):
            for row in range(int(start[1:]), int(end[1:])+1):
                res.append(chr(col)+str(row))
        return res
        
