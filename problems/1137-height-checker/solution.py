class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        '''
            first make a sorted array
            can we do with two pointers?
            
            [1,1,4,2,1,3]

            [1,1,4,2,1,3]
                 ^ ^
            [1,1,2,4,1,3]
                   ^ ^
            [1,1,2,1,3,4]

        '''
        sorted_array = sorted(heights.copy())
        cnt = 0
        for i,x in enumerate(heights):
            if x != sorted_array[i]:
                cnt+=1
        return cnt


