class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = len(nums) * [1]
        # for i,x in enumerate(nums):
        #     if i in dic.keys():
        #         dic[i].append(nums[i])
        pre = post = 1
        num_len = len(nums)
        cnt = 0
        for i in range(num_len):
            ans[i] *= pre
            pre = pre * nums[i]
            ans[num_len-i-1] *= post
            post = post*nums[num_len-i-1]

        return ans
