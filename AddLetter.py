from DeleteLetter import DeleteLetter
from Editor import Editor


class AddLetter(Editor):
    """
     A AddLetter class. Check if the misspelled_word from the user input
     could be real_word from the database bt add one letter.

     Args:
         delete_letter (DeleteLetter): To check if a word could be another word by
         delete a letter.
     """
    def __init__(self, delete_letter: DeleteLetter):
        self.delete_letter = delete_letter

    def edit(self, misspelled_word: str, real_word: str) -> int:
        """
        Check If misspelled_word could be real_word using delete_letter.
        Go over misspelled_word, delete each word iteratively and check if
        misspelled_word is real_word.
        :param misspelled_word: The misspelled word from user input.
        :param real_word: A possible word from the database.
        :return: The edit index or -1 if there isn't any edit.
        """
        return self.delete_letter.edit(real_word, misspelled_word)
