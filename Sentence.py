class Sentence:
    """A Sentence class.

    Args:
        sentence (str): The sentence.
        file_name (str): The file which hold the sentence.
        line_number (int): The line numbers of the line in the file.

    """
    def __init__(self, sentence: str, file_name: str, line_number: int):
        self._line_number = line_number
        self._sentence = sentence
        self._file_name = file_name

    @property
    def line_number(self):
        return self._line_number

    @property
    def sentence(self):
        return self._sentence

    @property
    def file_name(self):
        return self._file_name


