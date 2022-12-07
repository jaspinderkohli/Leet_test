class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1
        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if nums[mid] == target:
        #         return mid
        #     # if left half is sorted in ascending order
        #     elif nums[mid] >= nums[left]:
        #         # check if target is in left half
        #         if nums[left] <= target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     # if right half is sorted in ascending order
        #     else:
        #         # check if target is in right half
        #         if nums[mid] < target <= nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # return -1
