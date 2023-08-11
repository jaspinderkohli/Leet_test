class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            x = list(word)
            x.sort()
            x = ''.join(x)
            if x not in dic:
                dic[x] = [word]
            else:
                dic[x].extend([word])
        return dic.values()
