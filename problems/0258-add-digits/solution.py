class Solution:
    def addDigits(self, num: int) -> int:

        def digitsum(number):
            i=0
            tot_sum = 0
            while i < len(str(number)):
                tot_sum+= int(str(number)[i])
                i+=1
            if len(str(tot_sum)) < 2:
                return tot_sum
            else:
                return digitsum(tot_sum)
        return digitsum(num)



