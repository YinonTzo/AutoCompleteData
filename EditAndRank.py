class Editor:

    def __init__(self, editor):
        self.__editor = editor

    def edit(self, misspelled_word: str, real_word: str):
        self.__editor.edit(misspelled_word, real_word)

    @staticmethod
    def rank(user_input: str, misspelled_word_place: int, editing_place: int):
        return 0
