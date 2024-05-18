class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ''' 
        Example 1
            s = 'abc'
            t = 'bac

            op = 2

            how? ==>
                    s   t 
                'a' 0   1
                'b' 1   0
                'c' 2   2

                OP = 1 + 1 

        '''
        tot = 0
        # for i,x in enumerate(s):
        #     for j,y in enumerate(t):
        #         if x == y:
        #             tot += abs(i-j)
        # return tot
        s_map = {
            x: i for i, x in enumerate(s)
        }
        
        for j, y in enumerate(t):
            tot += abs(s_map[y] - j)
        return tot


        
