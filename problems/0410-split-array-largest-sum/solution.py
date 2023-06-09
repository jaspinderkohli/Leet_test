class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold):
            cnt = 1
            total = 0
            for num in nums:
                total +=num
                if total > threshold:
                    total = num
                    cnt+=1
                    if cnt > k:
                        return False
            return True
        
        l,r = max(nums), sum(nums)
        while l < r:
            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
