class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_num = [str(x) for x in digits]
        new = str(int(''.join(new_num)) + 1)
        return [int(x) for x in new]

