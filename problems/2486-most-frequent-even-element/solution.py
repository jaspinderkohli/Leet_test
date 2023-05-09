class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        maj_elem = {}
        for x in nums:
            if x %2 ==0 and x not in maj_elem:
                maj_elem[x] = 1
            elif x %2 ==0 and x in maj_elem:
                maj_elem[x] += 1
            else:
                pass

        myKeys = list(maj_elem.keys())
        myKeys.sort()

        maj_elem = {i: maj_elem[i] for i in myKeys}
        
        max_key = -1
        if maj_elem:
            max_key = max(maj_elem, key= lambda k: maj_elem[k])
        return max_key
