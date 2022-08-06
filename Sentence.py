
class Sentence:
    """A Sentence class.

    Args:
        sentence (str): The sentence.
        file_name (str): The file which hold the sentence.

    Attributes:
        sentence (str): The sentence.
        file_name (str): The file which hold the sentence.
    """
    def __init__(self, sentence: str, file_name: str):
        self.sentence = sentence
        self.file_name = file_name

    def get_sentence(self):
        return self.sentence

    def get_file_name(self):
        return self.file_name


