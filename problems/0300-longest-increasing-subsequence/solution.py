class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            INP = [10,9,2,5,3,7,101,18]
            OP = Len ( [2,3,7,101] ). ===> 4

            x = 0 --> 10 

            1. 2 loops 
            i = 10 , idx
            j = [idx_i+1 : ]
        '''
        tails = []
        for num in nums:
            left, right = 0, len(tails)
            # Binary search to find the insertion point for num in tails
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            # If num is larger than all elements in tails, append it
            if left == len(tails):
                tails.append(num)
            # Otherwise, replace the first element that is >= num
            else:
                tails[left] = num
        # Length of tails is the length of the longest increasing subsequence
        return len(tails)

    # # Test cases
    # test_cases = [
    #     [10, 9, 2, 5, 3, 7, 101, 18],
    #     [0, 1, 0, 3, 2, 3],
    #     [7, 7, 7, 7, 7, 7, 7]
    # ]

    # results = [lengthOfLIS(case) for case in test_cases]
    # results

