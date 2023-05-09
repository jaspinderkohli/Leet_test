class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_al = {}
        for i in nums:
            if i not in maj_al:
                maj_al[i] = 1
            else:
                maj_al[i] += 1
        max_key = max(maj_al, key=lambda k: maj_al[k])
        return max_key


