class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for i, sub in enumerate(words):
            if x in sub:
                res.append(i)
        return res
