class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        new = ''
        for num in nums:
            new += str(num)
        l = []
        for i in new:
            l.append(int(i))
        return l

