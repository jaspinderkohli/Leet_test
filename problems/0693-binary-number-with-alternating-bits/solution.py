class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bval = bin(n)[2:]
        cnt = 0
        f = []
        for i in range(len(bval)-1):
            if bval[i] != bval[i+1]:
                f.append('y')
            else:
                f.append('n')
        return(True if f.count('y') == len(bval)-1 else False)
             
        
