class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return(nums)
        # else:
        evn = []
        odd = []
        for x in nums:
            if x % 2 == 0:
                evn.append(x)
            else:
                odd.append(x)
        evn.extend(odd)
        return(evn)
        # nums.sort( key= lambda x : x % 2 )
        # return(nums)
