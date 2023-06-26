class Solution:
    def sumOfMultiples(self, n: int) -> int:
        nums = [3,5,7]
        s = 0
        divs = []
        for i in range(1,n+1):
            for num in nums:
                if i % num == 0 and i not in divs:
                    divs.append(i)
                    s+=i
        return s
