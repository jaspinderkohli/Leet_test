class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word = str(word)
        n = len(word)
        match1, match2, match3 = True, True, True
        
        for i in word:
            if not i.isupper():
                match1 = False
                break
        if match1:
            return True
        
        for i in word:
            if not i.islower():
                match2 = False
                break
        if match2:
            return True
        
        if not word[0].isupper():
            match3 = False
        if match3:
            for i in range(1, n):
                if word[i].isupper():
                    match3 = False
        if match3:
            return True

        # if not matching
        return False
