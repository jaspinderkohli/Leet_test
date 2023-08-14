class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = {} 
        
        for i,x in paths:
            city[i] = x
        for k,v in city.items():
            if city[k] not in city.keys():
                return city[k] 
