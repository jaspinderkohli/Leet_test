class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        lis = []
        for word in words:
            new = word.split(separator)
            new_l = [x for x in new if x]
            lis.extend(new_l)
        return lis

