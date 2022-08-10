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
        self._sentence = sentence
        self._file_name = file_name

    @property
    def sentence(self):
        return self._sentence

    @property
    def file_name(self):
        return self._file_name


