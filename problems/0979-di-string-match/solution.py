class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # Calculate the length of the given string
        n = len(s)

        # Initialize two pointers:
        # 'i' to keep track of the smallest number not yet placed in the permutation
        # 'd' to keep track of the largest number not yet placed in the permutation
        i, d = 0, n

        # Initialize the permutation list with zeros, one element longer than the string
        perm = [0] * (n + 1)

        # Iterate over the characters in the string, along with their indices
        for idx, char in enumerate(s):
            # If the character is 'I', place the smallest available number at the current index
            if char == 'I':
                perm[idx] = i
                i += 1  # Increment the smallest number pointer
            # If the character is 'D', place the largest available number at the current index
            else:  # char is 'D'
                perm[idx] = d
                d -= 1  # Decrement the largest number pointer
        
        # After placing all the numbers based on 'I' and 'D',
        # place the last remaining number at the end of the permutation
        perm[n] = i  # At this point, i == d, so we could also use d here

        # Return the completed permutation list
        return perm

