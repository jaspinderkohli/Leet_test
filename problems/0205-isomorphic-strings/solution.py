class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Check if the length of the two strings are equal
        if len(s) != len(t):
            return False
        
        # Initialize two dictionaries to store the mapping between the characters
        s_to_t = {}
        t_to_s = {}
        
        # Iterate over the characters in s and t
        for i in range(len(s)):
            # If the character is not already in the dictionaries, add the mapping
            if s[i] not in s_to_t and t[i] not in t_to_s:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            # If the character is already in the dictionaries, check if the mapping is the same as before
            elif s[i] in s_to_t and s_to_t[s[i]] == t[i]:
                # If the mapping is the same, continue to the next character
                continue
            # If the mapping is different, return False
            else:
                return False
        
        # If all characters in s and t are checked without returning False, the strings are isomorphic
        return True
