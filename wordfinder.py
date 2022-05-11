"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
    """
    def __init__(self, file_path):
        file = open(file_path)
        self.attr = self.read_file(file)
        word_count = len(self.attr)
        print(f"{word_count} words read")
        
    def read_file(self, file):
        return [word.strip() for word in file]

    def random(self):
        return random.choice(self.attr)
    

class SpecialWordFinder(WordFinder):
    def read_file(self, file):
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]