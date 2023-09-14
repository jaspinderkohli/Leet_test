class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        '''
            1, 2, 3
            3 types 

            1, 1, 2, 3
            2 types

            4,5,6,5

        '''
        candy_types = set(candyType)
        n = len(candyType)
        print(len(candy_types))
        if len(candy_types) < (n/2):
            return len(candy_types)
        elif len(candy_types) >= (n/2):
            return int(n/2)

