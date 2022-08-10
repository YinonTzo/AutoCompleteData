class MisspelledWordDetails:
    """
    A MisspelledWordDetails class. When some word in the user input isn't exist in
    the database, MisspelledWordDetails created with the word and the place in the
    user input.

    Args:
        misspelled_word (str): The misspelled word.
        misspelled_word_place (int): The place in the user input.
    """
    def __init__(self, misspelled_word: str, misspelled_word_place: int):
        self.misspelled_word = misspelled_word
        self.misspelled_word_place = misspelled_word_place
