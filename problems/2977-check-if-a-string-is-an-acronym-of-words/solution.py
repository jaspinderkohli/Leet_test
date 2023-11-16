class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        '''
            check for first letter and it to an array or string
        '''
        common = ''
        for word in words:
            common += word[0]
        return common == s

