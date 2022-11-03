class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # numBottles + numBottles/numExchange + (numBottles/numExchange)/numExchange till < numExchange
        # temp = numBottles
        res = numBottles
        while numBottles >= numExchange:
            numBottles, remain = int(numBottles/numExchange), numBottles % numExchange
            res += numBottles
            numBottles += remain
        return res
