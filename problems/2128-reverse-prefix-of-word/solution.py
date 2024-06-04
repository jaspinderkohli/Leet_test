class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        '''
            Example 1
                word = "abcdefd"
                        ^
                ch = d

                output => "dcbaefd"

            Example 2

                word = "xyxzxe"
                           ^
                ch = "z"
                op = "zxyxxe"


            Example 3
                Input: word = "abcd", ch = "z"
                Output: "abcd"

        '''

        l = 0
        
        # find first occurance
        r = None
        for i,x in enumerate(word):
            if x == ch:
                r = i
                break
        
        if not r:
            return word

        word = list(word)
        while l < r:
            word[l], word[r] = word[r], word[l]
            l+=1
            r-=1
        return "".join(word)
