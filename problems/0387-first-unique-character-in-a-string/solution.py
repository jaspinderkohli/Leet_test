class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = 1
            elif i in dic:
                dic[i] += 1
        print(dic)
        for i,x in enumerate(s):
            if dic[x] == 1:
                return i
        return -1
        
