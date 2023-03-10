class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # calculate the total sum of the input array
        left_sum = 0  # initialize left sum to 0
        for i in range(len(nums)):
            if left_sum == (total_sum - left_sum - nums[i]):  # if left sum is equal to right sum
                return i  # return the current index as pivot index
            left_sum += nums[i]  # add the current number to the left sum
        return -1  # if no such index exists, return -1
