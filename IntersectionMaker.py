from Data import Data
import MisspelledWordDetails


class IntersectionMaker:
    """
    IntersectionMaker class. Responsible to make the intersection of all the words from
    the user input that exist in database.

    Args:
        data (Data): The database.

    Attributes:
        data (Data): The database.
    """
    def __init__(self, data: Data):
        self.__data = data

    def find_intersections(self, prefix: str) -> tuple[list[MisspelledWordDetails], set[int]]:
        """
        Go over on the user input and check for every word if exists or not.
        If the word isn't exist in the database, add the word to the misspelled_words list.
        :param prefix: The user input.
        :return: Intersection of all the word that exist, and list of misspelled_words.
        """
        intersection_of_lines = set()
        misspelled_words = list()

        prefix_as_list = prefix.lower().split(" ")
        for i, word in enumerate(prefix_as_list):
            lines_numbers = self.__data.get_lines_from_word_to_sentence(word)
            if lines_numbers:
                intersection_of_lines = self.__make_intersection(intersection_of_lines, lines_numbers)
            else:
                misspelled_words.append(MisspelledWordDetails.MisspelledWordDetails(word, i))

        return misspelled_words, intersection_of_lines

    @staticmethod
    def __make_intersection(intersection_of_lines: set[int], lines_numbers: set[int]) -> set[int]:
        """
        Make the intersection between the old set and lines of the new word.
        :param intersection_of_lines: The intersection of all word.
        :param lines_numbers: The lines of the new word.
        :return: New set that contains the intersection of the 2 sets.
        """
        if intersection_of_lines:
            intersection_of_lines = intersection_of_lines.intersection(lines_numbers)
        else:
            intersection_of_lines = lines_numbers
        return intersection_of_lines
