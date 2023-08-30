class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # cnt = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if abs(nums[i] - nums[j]) == k and i < j:
        #             cnt+=1
        # return cnt

        '''
            using dict
        '''
        seen = defaultdict(int)
        cnt = 0
        for num in nums :
            tmp, tmp2 = num - k , num + k
            if tmp in seen:
                cnt += seen[tmp]
            if tmp2 in seen:
                cnt += seen[tmp2]

            seen[num] += 1
        return cnt
