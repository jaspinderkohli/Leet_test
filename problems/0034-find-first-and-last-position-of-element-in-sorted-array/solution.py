class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = end = -1

        l = 0
        r = len(nums)-1
        # SEARCH IN LEFT SIDE
        while l<=r:
            mid = (l+r ) // 2
            if nums[mid] == target:
                start = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l+=1
        l = 0
        r = len(nums)-1
        # SEARCH IN RIGHT SIDE
        while l<=r:
            mid = (l+r ) // 2
            if nums[mid] == target:
                end = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l+=1
            
        return [start, end]
