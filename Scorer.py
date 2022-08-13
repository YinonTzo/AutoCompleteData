class Scorer:
    """
    A Scorer base class. Responsible to calculate the base score and find the correct place
    where the editing was.
    """
    @staticmethod
    def calculate_editing_place(user_input: str, misspelled_word: str, editing_place: int):
        """
        Calculate the editing place.
        :param user_input: The user input.
        :param misspelled_word: The misspelled word from the user input.
        :param editing_place: The index in the misspelled word.
        :return: The real place of the editing in the user input.
        """
        return user_input.find(misspelled_word) + editing_place + 1

    def rank(self, user_input: str, misspelled_word: str, editing_place: int):
        pass

    @staticmethod
    def basic_score(user_input: str):
        """
        Calculate the basic score.
        :param user_input: The user input.
        :return: The basic score.
        """
        return 2 * len(user_input)
