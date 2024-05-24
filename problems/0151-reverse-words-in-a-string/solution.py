class Solution:
    def reverseWords(self, s: str) -> str:
        '''
            two pointers
            
            s = "the sky is blue"
                  ^         ^
                 blue sky is the
                      ^   ^
            OP = blue is sky the
            
            
        '''
        s = s.split()
        
        i, j = 0, len(s) -1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return ' '.join(s)
