class Solution:
    

    def countBeautifulPairs(self, nums: List[int]) -> int:

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def is_coprime(x, y):
            return gcd(x, y) == 1

        n = len(nums)
        beautiful_pairs = 0
        
        for i in range(n):
            for j in range(i+1, n):
                first_digit = nums[i] // 10**(len(str(nums[i])) - 1)
                last_digit = nums[j] % 10
                print(first_digit)

                if is_coprime(first_digit, last_digit):
                    beautiful_pairs += 1

        return beautiful_pairs
