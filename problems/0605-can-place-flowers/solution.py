class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
            flowerbed = [1,0,0,0,1], n = 1
            odd/even?
            tot = 5
            1's = 2
            0's = 3

            i-1, i+1

        '''
        length = len(flowerbed)
        ones = flowerbed.count(1)

        cnt = 0
        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                cnt += 1
                flowerbed[i] = 1
            if cnt >= n:
                return True
        return False

        
