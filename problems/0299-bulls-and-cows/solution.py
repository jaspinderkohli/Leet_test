class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        secret_count = {}  # To store occurrences of each digit in secret
        guess_count = {}   # To store occurrences of each digit in guess
        
        for i in range(len(secret)):
            s_digit = int(secret[i])
            g_digit = int(guess[i])
            
            if s_digit == g_digit:
                bulls += 1
            else:
                secret_count[s_digit] = secret_count.get(s_digit, 0) + 1
                guess_count[g_digit] = guess_count.get(g_digit, 0) + 1
        for digit, count in guess_count.items():
            if digit in secret_count:
                cows += min(count, secret_count[digit])
        
        return str(bulls) + 'A' + str(cows) + 'B'
