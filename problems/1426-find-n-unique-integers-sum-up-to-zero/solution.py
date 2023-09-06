class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n < 2:
            return [0]
        
        left = [ -i for i in range(1, int(n/2)+1, 1)]
        right = [ i for i in range(1, int(n/2)+1, 1)]
        left.extend(right)

        if n%2==0:
            return left
        else:
            left.append(0)
            return left

