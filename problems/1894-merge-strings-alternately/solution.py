class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        Example 1 

            w1 = 'abc'
            w2 = 'pqr'

            merged = 'apbqcr'
        
        Example 2
            w1 = 'ab'
            w2 = 'pqrs'

            merged = 'apbqrs'



        '''
        i = j = 0
        conc = ''
        while i < len(word1) and j < len(word2):
            conc += word1[i] + word2[j]
            # print(word1[i], word2[j])
            i+=1
            j+=1
        conc+= word1[i:]
        conc+= word2[j:]
        return conc



        


        
