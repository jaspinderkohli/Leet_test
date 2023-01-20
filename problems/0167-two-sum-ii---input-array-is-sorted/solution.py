class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        wanted_nums = {}
        for i in range(len(numbers)):
            if numbers[i] in wanted_nums:
			    return [wanted_nums[numbers[i]], i+1]
            else:
                wanted_nums[target - numbers[i]] = i+1
        return [-1, -1]
