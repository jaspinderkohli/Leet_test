class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
            Example 1 
                s = "hello"
                      ^  ^
                output = "holle"

            Example 2
                s = "leetcode"
                      ^     ^
                      leetcode
                        ^  ^
                      leotcede
                            break
                output = leotcede
        '''
        vowels = ['a','e','i','o','u','A','E','I', 'O', 'U']
        i, j = 0 , len(s)-1
        s = list(s)
        while i < j:
            if s[i] not in vowels:
                i+=1
                continue
            if s[j] not in vowels:
                j-=1
                continue

            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
        return ''.join(s)
            


