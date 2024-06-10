class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        '''
        Example 1
            IP = ["cat","bat","rat"]
            sent = "the cattle was rattled by the battery"

        '''
        dic = {
            
        }
        sentence = sentence.split()
        for word in dictionary:
            for match in sentence:
                if len(match) >= len(word):
                    if word == match[:len(word)]:
                        if match in dic.keys():
                            dic[match] = min(word, dic[match])
                        else:
                            dic[match] = word
        new_sent = ""
        for i, word in enumerate(sentence):
            if word in dic.keys():
                sentence[i] = dic[word]
        return " ".join(sentence)

