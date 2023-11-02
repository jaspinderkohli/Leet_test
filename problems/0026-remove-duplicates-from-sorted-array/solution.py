class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # '''
        #     if doesnt exist in dict means it's unique
        #     add it to nums and increase the cntr

        # '''
        # dic = {}
        # cnt = 0
        # for i,x in enumerate(nums):
        #     if x not in dic:
        #         nums[cnt] = x
        #         dic[x] = i
        #         cnt+=1
        # return cnt
        dic = {}
        cnt = 0
        for i,x in enumerate(nums):
            if x not in dic.values():
                dic[i] = x
                nums[cnt] = x
                cnt+=1
        return cnt
