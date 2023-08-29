class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode_map = {}
        asc_val = 97
        for char in key:
            if char not in decode_map.keys() and char != ' ':
                decode_map[char] = chr(asc_val)
                asc_val+=1
        # decode 
        decoded_message = ""
        for word in message:
            if word == ' ':
                decoded_message+= ' '    
            else:
                decoded_message += decode_map[word]
        return decoded_message

            
        

