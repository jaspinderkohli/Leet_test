class Solution:
    def isHappy(self, n: int) -> bool:
        # # Define the happy_number function that takes a number and a set of visited numbers as input
        # def happy_number(n, visited=set()):
        #     # Initialize the total sum to 0
        #     total_sum = 0
        #     # Iterate over the digits of the number
        #     for digit in str(n):
        #         # Add the square of each digit to the total sum
        #         total_sum += int(digit) ** 2
        #     # If the total sum is 1, return True (the number is happy)
        #     if total_sum == 1:
        #         return True
        #     # If the total sum has been seen before, return False (there is a cycle)
        #     elif total_sum in visited:
        #         return False
        #     # Otherwise, add the total sum to the set of visited numbers and recurse with the new number
        #     else:
        #         visited.add(total_sum)
        #         return happy_number(total_sum, visited)
        
        # # Call the happy_number function with the input number and return the result
        # return happy_number(n)
        def happy_number(n, visited=set()):
            tot_sum = 0
            for dig in str(n):
                tot_sum += int(dig) ** 2
            
            if tot_sum == 1:
                return True
            elif tot_sum in visited:
                return False

            else:
                visited.add(tot_sum)
                return happy_number(tot_sum, visited)
        
        return happy_number(n)


