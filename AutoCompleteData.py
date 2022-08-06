from dataclasses import dataclass


@dataclass
class AutoCompleteData:

    def __init__(self, completed_sentence, source_text, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def __str__(self):
        return self.completed_sentence + " (" + self.source_text + " " + str(self.offset) + ")"

    def __repr__(self):
        return self.completed_sentence + " (" + self.source_text + " " + str(self.offset) + ")"
