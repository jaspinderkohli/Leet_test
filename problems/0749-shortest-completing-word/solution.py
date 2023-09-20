class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join(filter(str.isalpha, licensePlate.lower()))
        print(licensePlate)

        plate_counts = collections.Counter(licensePlate)
        print(plate_counts)

        shortest_word = None
        shortest_length = float('inf')

        # Iterate through the words
        for word in words:
            # Create a Counter for the characters in the current word
            word_counts = collections.Counter(word)

            # Check if the current word contains all characters in licensePlate
            if all(word_counts[char] >= plate_counts[char] for char in plate_counts):
                # If it's shorter than the current shortest word, update the shortest word
                if len(word) < shortest_length:
                    shortest_word = word
                    shortest_length = len(word)

        return shortest_word
