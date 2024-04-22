class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
            s = "barfoothefoobarman"
            words = ["foo","bar"]

        '''
        from collections import Counter

        # Each word is of the same length
        word_length = len(words[0])
        # Total number of words
        word_count = len(words)
        # Total length of the substring we need to find
        total_length = word_length * word_count
        # Frequency of each word in the list 'words'
        word_freq = Counter(words)
        # Result list to store starting indices of valid substrings
        res = []

        # We start from different positions in the word's length to cover all cases
        for i in range(word_length):
            # 'left' defines the start of our current sliding window
            left = i
            # 'count' tracks the number of valid words found in the current window
            count = 0
            # Current frequency of words in the sliding window
            cur_freq = Counter()

            # Move 'j' in steps of 'word_length' to check every possible word
            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j:j+word_length]
                # Only consider the word if it's in 'words'
                if word in word_freq:
                    cur_freq[word] += 1
                    count += 1

                    # If a word occurs more than expected, reduce the window size
                    while cur_freq[word] > word_freq[word]:
                        left_word = s[left:left+word_length]
                        cur_freq[left_word] -= 1
                        count -= 1
                        left += word_length
                    
                    # If we have the right number of valid words, record the starting index
                    if count == word_count:
                        res.append(left)
                else:
                    # If a non-matching word is found, reset and move the window
                    cur_freq.clear()
                    count = 0
                    left = j + word_length

        return res
