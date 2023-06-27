class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()[:k]
        return ' '.join(words)
