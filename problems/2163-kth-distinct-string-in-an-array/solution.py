class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        '''
            arr = ["d","b","c","b","c","a"]
            k = 2
        '''
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        
        cntr = 1
        for key,val in dic.items():
            if val <=1:
                if cntr == k:
                    return key
                cntr+=1
        return ""


