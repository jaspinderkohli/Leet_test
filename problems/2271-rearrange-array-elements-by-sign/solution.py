class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''
            inp = [3,1,-2,-5,2,-4]
            op =  [3,-2,1,-5,2,-4]

            
            
            sort positives and negatives?
            maybe 2 arrays ?? 
            then 1 from positive 1 from negative

        '''
        pos = []
        neg = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        idx_pos = 0
        idx_num = 0 
        while idx_num < len(nums):
            nums[idx_num], nums[idx_num+1] = pos[idx_pos], neg[idx_pos]
            idx_num += 2
            idx_pos +=1
        return nums


