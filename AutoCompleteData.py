from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    complete_sentence_id: int
    completed_sentence: str
    source_text: str
    offset: int
    score: int
    file_name: str

    def __init__(self, complete_sentence_id, completed_sentence, source_text, offset, score, file_name):
        self.completed_sentence_id = complete_sentence_id
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score
        self.file_name = file_name

    def get_id(self):
        return self.completed_sentence_id

    def get_str(self):
        return (self.source_text + " (" + self.file_name + " " + str(self.offset) + ")")
