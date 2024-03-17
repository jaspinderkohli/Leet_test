class Solution:
    def originalDigits(self, s: str) -> str:
        # Step 1: Count occurrences of each unique letter
        count = [0] * 10
        for char in s:
            if char == 'z':
                count[0] += 1
            elif char == 'w':
                count[2] += 1
            elif char == 'u':
                count[4] += 1
            elif char == 'x':
                count[6] += 1
            elif char == 'g':
                count[8] += 1
            elif char == 'o': # After deducting counts for 0, 2, 4, 6
                count[1] += 1
            elif char == 'h': # After deducting counts for 3, 8
                count[3] += 1
            elif char == 'f': # After deducting counts for 4
                count[5] += 1
            elif char == 's': # After deducting counts for 6
                count[7] += 1
            elif char == 'i': # After deducting counts for 5, 6, 8
                count[9] += 1
        
        # Deduct counts for each digit
        count[1] -= count[0] + count[2] + count[4]
        count[3] -= count[8]
        count[5] -= count[4]
        count[7] -= count[6]
        count[9] -= count[5] + count[6] + count[8]

        # Reconstruct the digits
        digits = ""
        for i in range(10):
            digits += str(i) * count[i]

        return digits
