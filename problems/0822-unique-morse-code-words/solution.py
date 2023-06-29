class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # for mapping
        dic = {
        }

        val = 97
        for code in codes:
            dic[chr(val)] = code
            val+=1

        # encoded part
        encoded_dic = {}
        for word in words:
            enc = ''
            for char in word:
                enc += dic[char] 
            encoded_dic[enc] = word
        return len(encoded_dic.keys())
