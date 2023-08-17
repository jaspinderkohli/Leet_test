class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lis_n = [x for x in range(1,n+1)]
        def findWin(lis_n, index):
            if len(lis_n) == 1:
                return lis_n[0]
            else:
                index = (index + k -1) % len(lis_n)
                lis_n.pop(index)
                return findWin(lis_n, index)
        
        return findWin(lis_n, 0)


