class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return nums
        start = end = nums[0]
        ranges = []
        for i in range(1,len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + '->'+str(end))
                start = nums[i]
                end = nums[i]
        # Add the last range
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(end))
        return ranges

