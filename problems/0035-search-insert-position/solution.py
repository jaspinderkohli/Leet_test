class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = False
        for i in range(len(nums)):
            if nums[i] == target:
                found=True
                # return(i)
                break;
            else:
                continue
        if not found:
            nums.append(target)
            nums.sort()
            # print(nums)
        
        return(nums.index(target))
        # print(found)
