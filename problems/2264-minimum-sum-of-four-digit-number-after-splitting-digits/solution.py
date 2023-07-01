class Solution:
    def minimumSum(self, num: int) -> int:
        '''
            [1, 2, 3, 4]
            [1, 3]
            [2, 4]
            1. first sort
            2. Add alternate numbers to 1st 
        '''
        digits = sorted(str(num))
        new1 = ""
        new2 = ""

        for i, digit in enumerate(digits):
            if i % 2 == 0:
                new1 += digit
            else:
                new2 += digit

        return int(new1) + int(new2)
