from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int
    file_name: str

    def __init__(self, completed_sentence, source_text, offset, score, file_name):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score
        self.file_name = file_name

    def print(self):
        print(self.source_text + " (" + self.file_name + " " + self.offset + ")")
