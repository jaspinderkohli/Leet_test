class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i,x in enumerate(nums):
        #     if x == target:
        #         return(i)
        # return(-1)
        """ 
            Using binary serarch 
            l 0
            h last element
        """
        l=0
        h=len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return -1

            

