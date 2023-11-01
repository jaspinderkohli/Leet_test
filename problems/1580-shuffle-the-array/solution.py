class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # '''
        #     keep 2 counters 1 for ans and 1 for nums
        # '''
        # ans = len(nums) * [None]
        # i=cnt=0
        # while i < n:
        #     ans[cnt],ans[cnt+1] = nums[i], nums[i+n]
        #     i+=1
        #     cnt+=2
        # return ans
        new = 2 * n * [None]
        cnt = 0
        for i in range(0,n):
            new[cnt], new[cnt+1] = nums[i], nums[i+n]
            cnt+=2
        return new



