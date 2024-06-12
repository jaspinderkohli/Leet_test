class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # """
        # Do not return anything, modify nums in-place instead.
        # """
        # # just make one list for each color
        # zer = []
        # one = []
        # two = []
        # for x in nums:
        #     if x == 0:
        #         zer.append(x)
        #     elif x == 2:
        #         two.append(x)
        #     else:
        #         one.append(x)
        # # merge these lists and replace them with nums by iterating
        # nums_cpy = zer+one+two
        # for i,x in enumerate(nums_cpy):
        #     nums[i] = x

        ''' 
            0s 1s and 2s

            Example 1 
                nums = [2,0,2,1,1,0]
                output = [0,0,1,1,2,2]
                make a dict with counts

        '''
        dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        n = len(nums)
        balls = 0
        idx = 0
        for i in range(3):
            if i in dic:
                while dic[i]:
                    nums[idx] = i
                    idx+=1
                    dic[i]-=1
