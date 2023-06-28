class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt=0
        for word in words:
            consistent = True
            for i in word:
                if i not in allowed:
                    consistent = False
                    break

            if consistent:
                cnt+=1

        return cnt
