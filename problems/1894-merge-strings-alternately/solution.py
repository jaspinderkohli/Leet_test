class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
            word1 = a b c
            word2 =  p q r
        '''
        
        max_len = max(len(word1), len(word2)) - 1
        min_len = min(len(word1), len(word2)) - 1
        out =''
        for i in range(max_len+1):
            if i <= min_len:
                out += word1[i] + word2[i]
            else:
                if max_len == len(word1)-1:
                    out += word1[i]
                else:
                    out += word2[i]
        return out
            
