class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        N = len(words)

        word_dic = { word[-1]: word[:-1] for word in words}
        print(word_dic)

        sent = ''
        for i in range(1, N + 1):
            sent += word_dic[str(i)]
            if i < N:
                sent += ' '
        return sent
        
