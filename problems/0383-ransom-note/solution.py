class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        need two hashmaps, one with freq from magazine, other with freq of 
        ransomNote. is each freq in ransomNote is <= that freq in magazine, it is cool, otherwise bail
        '''
        def buildFreq(string):
            res = {}
            for char in string:
                if char in res:
                    res[char] += 1
                else:
                    res[char] = 1
            return res
        
        ransomFreq = buildFreq(ransomNote)
        magazineFreq = buildFreq(magazine)
        
        for key in ransomFreq.keys():
            if key not in magazineFreq:
                return False
            if ransomFreq[key] > magazineFreq[key]:
                return False
        
        return True
