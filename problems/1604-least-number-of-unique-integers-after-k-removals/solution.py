class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        '''
            Example 1 

            arr = [5, 5, 4] k = 1
            oupt = 1

            remove 1 element ==> [5, 5] 

            Example 2
            arr = [4,3,1,1,3,3,2], k = 3

            remove 3 elements ==> 4, 2, 
        '''
        cntr = Counter(arr)
        set_arr = set(arr)
        
        least_common_to_most = sorted(cntr, key=lambda x: cntr[x])
        i = 0

        while k > 0:
            if cntr[least_common_to_most[i]] <= k:
                set_arr.remove(least_common_to_most[i])
                k -= cntr[least_common_to_most[i]]
                i += 1
            else:
                break

        return len(set_arr)

