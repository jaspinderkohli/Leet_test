class Solution:
    def isHappy(self, n: int) -> bool:
        # Set to keep track of numbers encountered during the process
        hset = set()

        # Continue the loop until the number becomes 1
        while n != 1:
            # Check if the current number is already in the set, indicating a cycle
            if n in hset:
                return False  # If a cycle is detected, the number is not a happy number

            # Add the current number to the set, marking it as visited
            hset.add(n)

            # Calculate the sum of the squares of each digit and update the current number
            n = sum([int(i) ** 2 for i in str(n)])

        # If the loop exits with the number being 1, it is a happy number
        else:
            return True


