class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21]
        # number : number % num === 0
        
        lis = [val for val in range(left, right+1) if '0' not in str(val)]
        lis1 = lis.copy()
        print(lis1)
        
        for num in lis:
            for x in str(num):
                if num % int(x) == 0:
                    pass
                elif num % int(x) != 0:
                    lis1.remove(num)
                    break
        return(lis1)
