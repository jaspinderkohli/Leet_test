class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dic = {}
        cnt = 0
        for word in words:
            word =  ''.join(sorted(word))
            if word  not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
                cnt+=1
        return cnt


