from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
            if 2nd pair is unique return 

        '''
        d = {}
        for i in range(1, n+1):
            d[i] = 0


        for x,y in trust:
            d[y] += 1
        print(d)

        trust2 = [x for x,y in trust]
        for i in range(1,n+1):
            if i not in trust2 and d[i] == n-1:
                return i
                

        return -1
