from Editor import Editor


class EditAndRank:
    """
    An EditAndRank class. contain editor and scorer.

    Args:
        editor (Editor) : some derived object from Editor.
    """
    def __init__(self, editor: Editor):
        self.__editor = editor

    def edit(self, misspelled_word: str, real_word: str):
        return self.__editor.edit(misspelled_word, real_word)

    @staticmethod
    def rank(user_input: str, misspelled_word_place: int, editing_place: int):
        return 0
