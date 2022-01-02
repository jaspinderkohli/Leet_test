class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        new_dic = {}
        for x in nums:
            if x in new_dic:
                new_dic[x] += 1
            else:
                new_dic[x] = 1

        for key, val in new_dic.items():
            if val >= 2:
                return key
