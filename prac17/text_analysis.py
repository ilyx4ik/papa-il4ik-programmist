from collections import Counter

class TextStats:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())

    def most_common_letter(self):
        
        letters = [char.lower() for char in self.text if char.isalpha()]
        if not letters:
            return None
        counter = Counter(letters)
        return counter.most_common(1)[0]