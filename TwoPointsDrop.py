from Scorer import Scorer


class TwoPointsDrop(Scorer):
    """
    Derived class from Scorer.
    """
    def rank(self, user_input: str, misspelled_word: str, editing_place: int):
        """
        Drop points from the basic score. Drop 2 points for each editing,
        but if the editing were in the beginning, it would drop more points.
        :param user_input: The user input.
        :param misspelled_word: The misspelled word from the user input.
        :param editing_place: The index in the misspelled word.
        :return: The score of the user input.
        """
        editing_place_in_user_input = self.calculate_editing_place(user_input, misspelled_word, editing_place)
        if editing_place_in_user_input > 4:
            return self.basic_score(user_input) - 2
        if editing_place_in_user_input == 4:
            return self.basic_score(user_input) - 4
        if editing_place_in_user_input == 3:
            return self.basic_score(user_input) - 6
        if editing_place_in_user_input == 2:
            return self.basic_score(user_input) - 8
        if editing_place_in_user_input == 1:
            return self.basic_score(user_input) - 10
