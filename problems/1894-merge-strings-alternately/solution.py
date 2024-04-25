class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        word1 = "abc"
        word2 = "pqr"
        res = "apbqcr"

        ques1 = lentgh same?
        
        cntr i,j = 0

        '''
        i = j = 0
        conc = ''
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                conc += word1[i]
                i+=1
            if j < len(word2):
                conc += word2[j]
                j+=1
        return conc

        


        
