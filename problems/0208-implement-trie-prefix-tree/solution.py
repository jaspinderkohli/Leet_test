class Trie:

    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        if word not in self.dic:
            self.dic[word] = 1

    def search(self, word: str) -> bool:
        if word in self.dic.keys():
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        pre_len = len(prefix)
        for key in self.dic.keys():
            if key[:pre_len] == prefix:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
