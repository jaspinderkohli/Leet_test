class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        new = sentence.split(' ')
        for i,x in enumerate(new):
            if searchWord == x[:len(searchWord)]:
                return i+1
        return -1
