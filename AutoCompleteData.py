from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    """A AutoCompleteData class.

        Args:
            complete_sentence (str): The completed_sentence.
            source_text (str): Where the sentence comes from.
            offset (int): Where the user input starts relative to the complete sentence.
            score (int): The score of this sentence.

        Attributes:

        """
    def __init__(self, complete_sentence: str, source_text: str, offset: int, score: int):
        self.complete_sentence = complete_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def __str__(self):
        return self.complete_sentence + " (" + self.source_text + " " + str(self.offset) + ")"

    def __repr__(self):
        return self.complete_sentence + " (" + self.source_text + " " + str(self.offset) + ")"
