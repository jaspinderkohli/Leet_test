class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic1 = {}
        for x in items1:
            dic1[x[0]] = x[1]
        for x in items2:
            if x[0] in dic1:
                dic1[x[0]] += x[1]
            else:
                dic1[x[0]] = x[1]
        dic1 = sorted(dic1.items())
        return [list(x) for x in dic1]
        
        
