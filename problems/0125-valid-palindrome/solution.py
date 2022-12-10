class Solution:
    def isPalindrome(self, s: str) -> bool:
        # for x in s:
        #     if (65 <= ord(x) <= 90) or (97 <= ord(x) <= 122) or (48 <= ord(x) <= 57):
        #         pass
        #     else:
        #         s = s.replace(x,'')
        # s = s.lower()
        # return s == s[::-1]
        s = s.lower()

        # Remove all non-alphanumeric characters
        s = ''.join(c for c in s if c.isalnum())

        # Check if the string is a palindrome
        return s == s[::-1]
