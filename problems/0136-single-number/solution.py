class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_dic = {}
        for i in range(0,len(nums)):
            if nums[i] not in new_dic:
                new_dic[nums[i]] = 1
            else:
                new_dic.pop(nums[i])
        for key in new_dic:
            return key
