class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l <=r :
            mid = (l+r) // 2
            if nums[mid] == target:
                first = last = mid
                if first >= 0:
                    while first != 0 and nums[first] == nums[first-1]:
                        first-=1
                # find last occurrence
                if last != len(nums) - 1:
                    while last != len(nums) - 1 and nums[last] == nums[last+1]:
                        last += 1
                else:
                    # only one 'target' was found
                    return [first]
                return list(range(first,last+1))
                
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        
