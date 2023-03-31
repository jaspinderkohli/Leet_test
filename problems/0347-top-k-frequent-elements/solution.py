class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Approach:
        1. Count the frequency of each element in nums using a dictionary
        2. Sort the dictionary items by frequency in descending order
        3. Select the top k elements from the sorted dictionary items and return them

        Time complexity: O(nlogn) due to sorting
        Space complexity: O(n) for the dictionary
        '''
        # Step 1: Count the frequency of each element in nums using a dictionary
        elements = {}
        for x in nums:
            if x not in elements:
                elements[x] = 1
            else:
                elements[x] += 1

        # Step 2: Sort the dictionary items by frequency in descending order
        sorted_dic = sorted(elements.items(), key=lambda x:x[1], reverse=True)

        # Step 3: Select the top k elements from the sorted dictionary items and return them
        lis = []
        for i in range(k):
            lis.append(sorted_dic[i][0])
        return lis

