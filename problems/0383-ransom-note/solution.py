class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        for x in ransomNote:
            if x not in ransomNote_dict:
                ransomNote_dict[x] = 1
            else:
                ransomNote_dict[x] +=1

        magazine_dict = {}
        for x in magazine:
            if x not in magazine_dict:
                magazine_dict[x] = 1
            else:
                magazine_dict[x] +=1

        for y in ransomNote_dict:
            try:
                if ransomNote_dict[y] > magazine_dict[y]:
                    return False
            except:
                return False
        return True


