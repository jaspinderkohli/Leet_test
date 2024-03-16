class Solution:
    def romanToInt(self, s: str) -> int:
        '''
            ex 1 
                Inp = "III"
                output = 3

            ex2 
                Inp = "LIV"
                op = "5 - 1 + 50" ==> 54
        '''
        n = len(s)
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        prev_value = 0
        
        for i in range(n - 1, -1, -1):
            current_value = m[s[i]]
            if current_value < prev_value:
                ans -= current_value
            else:
                ans += current_value
            prev_value = current_value
        
        return ans
