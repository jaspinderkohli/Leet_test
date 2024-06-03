class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            Example 1

                s = "abcabcbb"
                output 3 -> 'a b c'

            Exmample 2
                s = "bbbbb"
                output 1 -> 'b'

            Example 3 
                s = "pwwkew"
                ==> pw / wke / ew
                ouput 3

            new_str = ''

        '''
        
        
        l, r = 0, 0

        if not len(s):
            return 0

        char_set = set()
        max_len = 0

        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                max_len = max(max_len, len(s[l:r+1]))
                r+=1
            else:
                char_set.remove(s[l])
                l+=1
        return max_len

        
