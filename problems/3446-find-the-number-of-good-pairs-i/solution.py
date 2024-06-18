class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''

        '''
        freq = {}
    
        # Compute the required divisors and store their frequencies in the hash map
        for num in nums2:
            divisor = num * k
            if divisor in freq:
                freq[divisor] += 1
            else:
                freq[divisor] = 1
        
        count = 0
        # Check for good pairs
        for num in nums1:
            for divisor in freq:
                if num % divisor == 0:
                    count += freq[divisor]
        
        return count
