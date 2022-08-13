from Editor import Editor
from Scorer import Scorer


class EditAndRank:
    """
    An EditAndRank class. contain editor and scorer.

    Args:
        editor (Editor) : Some derived object from Editor.
        scorer (Scorer) : Some derived object from Scorer.
    """
    def __init__(self, editor: Editor, scorer: Scorer):
        self.__scorer = scorer
        self.__editor = editor

    def edit(self, misspelled_word: str, real_word: str):
        return self.__editor.edit(misspelled_word, real_word)

    def rank(self, user_input: str, misspelled_word: str, editing_place: int):
        return self.__scorer.rank(user_input, misspelled_word, editing_place)
