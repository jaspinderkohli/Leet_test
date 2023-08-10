class Solution:
    def numTeams(self, rating: List[int]) -> int:
        '''
            dp 
        '''
        n = len(rating)
        count = 0

        # Arrays to store counts of soldiers with ratings smaller and greater than current soldier
        smaller = [0] * n
        greater = [0] * n

        # Count the number of soldiers with smaller and greater ratings for each soldier
        for i in range(n):
            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    greater[i] += 1
                elif rating[i] > rating[j]:
                    smaller[i] += 1

        # Calculate the number of teams based on the counts
        for i in range(n):
            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    count += greater[j]  # Count teams where current soldier is the middle one
                elif rating[i] > rating[j]:
                    count += smaller[j]  # Count teams where current soldier is the middle one

        return count

