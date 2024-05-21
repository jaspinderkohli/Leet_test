class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}

        for x in arr:
            if x not in dic.keys():
                dic[x] = 1
            else:
                dic[x] += 1

        un = []
        for x in dic.values():
            if x not in un:
                un.append(x)
            else:
                return False
        return True

