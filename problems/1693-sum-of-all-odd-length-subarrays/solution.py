class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        tot_sum = 0
        for i in range(n):
            for j in range(i,n):
                subarray = arr[i:j+1]
                if len(subarray) %2 ==1:
                    tot_sum += sum(subarray)
                    # tests12
        return tot_sum
        

