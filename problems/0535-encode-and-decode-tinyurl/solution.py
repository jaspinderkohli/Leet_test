class Codec:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_url = self.base_url + str(self.counter)
        self.url_mapping[short_url] = longUrl
        self.counter += 1
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_mapping.get(shortUrl, "")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
