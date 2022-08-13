from Editor import Editor


class ChangeLetter(Editor):
    """
     A ChangeLetter class. Check if the misspelled_word from the user input
     could be real_word from the database by change one letter in misspelled_word.
    """
    def edit(self, misspelled_word: str, real_word: str) -> int:
        """
        Check If misspelled_word could be real_word.
        Go over misspelled_word, split it to prefix and suffix iteratively and check if
        misspelled_word is real_word.
        :param misspelled_word: The misspelled word from user input.
        :param real_word: A possible word from the database.
        :return: The edit index or -1 if there isn't any edit.
        """
        for i in range(0, len(misspelled_word)):
            if misspelled_word[:i] == real_word[:i] and \
                    misspelled_word[i + 1:] == real_word[i + 1:]:
                return i
        return -1
