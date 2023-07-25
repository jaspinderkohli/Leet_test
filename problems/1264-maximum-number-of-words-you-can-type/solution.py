class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        '''
            1. split
            2, Each char if in each word then no
        '''
        text = text.split()
        length = len(text)
        brokenLetters = set(brokenLetters)

        for word in text:
            for char in word:
                if char in brokenLetters:
                    length -= 1
                    break
					
        return length
        

