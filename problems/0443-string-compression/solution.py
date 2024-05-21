class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
            Example 1
                
                chars = ["a","a","b","b","c","c","c"]
                conc = 'a2b2c3'
                return len(conc) ==> 6

            Example 2 

                chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
                conc = 'ab12'
                return len(conc) ==> 4

                

            Example 4 

        '''

        n = len(chars)
        cnt = 1
        conc = ''
        i=1
        while i < n:
            if chars[i] == chars[i-1]:
                cnt +=1
            elif chars[i] != chars[i-1]:
                if cnt > 1:
                    conc += chars[i-1] + str(cnt)
                else:
                    conc += chars[i-1]
                cnt = 1
            i+=1
            
        # Add the last processed character group
        if cnt > 1:
            conc += chars[i - 1] + str(cnt)
        else:
            conc += chars[i - 1]

        for i in range(len(conc)):
            chars[i] = conc[i]

        return len(conc)

