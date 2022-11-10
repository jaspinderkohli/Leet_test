class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # just make one list for each color
        zer = []
        one = []
        two = []
        for x in nums:
            if x == 0:
                zer.append(x)
            elif x == 2:
                two.append(x)
            else:
                one.append(x)
        # merge these lists and replace them with nums by iterating
        nums_cpy = zer+one+two
        for i,x in enumerate(nums_cpy):
            nums[i] = x
