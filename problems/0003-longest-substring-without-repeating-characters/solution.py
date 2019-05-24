class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # list = ''
        # for x in s:
        #     if x not in list :
        #         list+=x
        #     else:
        #         break
        # print list
        # for i in range(0,len(s)):
        #     word = set()
        #     for j in range(i,len(s)):
        #         if s[j] in word:
        #             break
        #         word.add(s[j])
        #     return word
        
        left_most_valid = 0
        longest = 0
        last_seen = {}

        for i, letter in enumerate(s):
            if letter in last_seen:
                # left_most_valid must be greater than any position which has been seen again
                left_most_valid = max(left_most_valid, last_seen[letter] + 1)
            last_seen[letter] = i

            # Length of substring from left_most_valid to i is i - left_most_valid + 1
            longest = max(longest, i - left_most_valid + 1)

        return longest
