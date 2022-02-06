class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_d = {
        }
        nums2_d = {}
        for i in nums1:
            if i in nums1_d:
                nums1_d[i]+=1
            else:
                nums1_d[i]=1
        for i in nums2:
            if i in nums2_d:
                nums2_d[i]+=1
            else:
                nums2_d[i]=1
        
        cmn = list(nums1_d.keys() & nums2_d.keys())
        new_l = []
        for k in cmn:
            min_v = min(nums1_d[k],nums2_d[k])
            new_l.extend([k]*min_v)
        return(new_l)
        
        
        
