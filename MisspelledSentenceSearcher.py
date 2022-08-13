import Clean_line
from AddLetter import AddLetter
from ChangeLetter import ChangeLetter
from Data import Data
from AutoCompleteData import AutoCompleteData
from CompleteSentenceSearcher import CompleteSentenceSearcher
import MisspelledWordDetails
from DeleteLetter import DeleteLetter
from EditAndRank import EditAndRank
from OnePointDrop import OnePointDrop
from TwoPointsDrop import TwoPointsDrop


class MisspelledSentenceSearcher:
    """
    A MisspelledSentenceSearcher. If there is one word with mistake,
    MisspelledSentenceSearcher will check if it is editable, rank it using Score,
    save the correct sentences in a sorted list and return the answers to controller.

    Args:
         data (Data):The database.
         complete_sentence_searcher (CompleteSentenceSearcher): If the misspelled word
         in the last word in the user input, the sentence is good and need to find all sentence
         in database.

    Attributes:
         editors (list[Editor]): Each editor is one of the check that could be.
    """
    def __init__(self, data: Data, complete_sentence_searcher: CompleteSentenceSearcher):
        self.__data = data
        self.__complete_sentence_searcher = complete_sentence_searcher
        self.__editors = self.__create_editors()

    def edit_sentences(self, user_input: str,
                       misspelled_word: MisspelledWordDetails,
                       intersection_of_lines: set[int]):
        """
        Split the sentence around the misspelled word,
        check for each line in the intersection if the prefix and the suffix are exists there.
        If so, tried to edit the misspelled word to be the same word as the real word in the line.
        :param user_input: The user input.
        :param misspelled_word: The misspelled word and its index in the user input.
        :param intersection_of_lines: The lines that contain the words from the user input.
        :return: A sorted list with the correct sentences. The list sort by the score.
        """
        split_user_input = user_input.split(" ")
        prefix = split_user_input[:misspelled_word.misspelled_word_place]
        suffix = split_user_input[misspelled_word.misspelled_word_place + 1:]

        fixed_sentences = list()
        for line in intersection_of_lines:
            split_sentence = Clean_line.clean_line_from_redundant_letters(self.__data.get_sentence_to_file(line).
                                                                          sentence).split(" ")

            first_match_index = self.__find_first_match(split_sentence, prefix)
            real_word_index = first_match_index + len(prefix)

            if self.__check_pattern_match(first_match_index, split_sentence, prefix) and \
                    self.__check_pattern_match(real_word_index + 1, split_sentence, suffix):

                edit = False
                for editor in self.__editors:
                    editing_place = editor.edit(misspelled_word.misspelled_word,
                                                split_sentence[real_word_index])
                    if editing_place != -1:
                        edit = True
                        score = editor.rank(user_input,
                                            misspelled_word.misspelled_word, editing_place)
                        fixed_sentences.append(AutoCompleteData(
                            self.__data.get_sentence_to_file(line).sentence,
                            self.__data.get_sentence_to_file(line).file_name,
                            self.__data.get_sentence_to_file(line).line_number,
                            score))
                if not edit and len(suffix) == 0:  # it means that all the words are ok but the last.
                    fixed_sentences = fixed_sentences + (self.__complete_sentence_searcher.
                                                         find_complete_sentence(user_input,
                                                                                intersection_of_lines))

        fixed_sentences.sort(key=lambda auto_complete: auto_complete.score)
        return fixed_sentences

    @staticmethod
    def __check_pattern_match(index: int, complete_sentence: list[str], partial_input: list[str]) -> bool:
        """
        Check if complete_sentence is equal to partial_input from the index that wes given.
        :param index: First index to looking for partial input in complete_sentence.
        :param complete_sentence: To check if contains partial_input. It is a line
        from the intersection.
        :param partial_input: Prefix or suffix from the user input.
        :return: True if complete_sentence is partial_input.
        """
        if len(partial_input) > len(complete_sentence[index:]):
            return False
        if len(partial_input) == 0:
            return True

        for i in range(0, len(partial_input)):
            if complete_sentence[index + i] != partial_input[i]:
                return False
        return True

    @staticmethod
    def __create_editors():
        """
        Create a list of EditorsAndRank.
        :return: a list of EditorsAndRank.
        """
        list_editors = list()
        delete_letter = DeleteLetter()
        two_points_drop = TwoPointsDrop()

        list_editors.append(EditAndRank(delete_letter, two_points_drop))
        list_editors.append(EditAndRank(AddLetter(delete_letter), two_points_drop))
        list_editors.append(EditAndRank(ChangeLetter(), OnePointDrop()))
        return list_editors

    @staticmethod
    def __find_first_match(split_sentence: list[str], prefix: list[str]):
        """
        Find the index where the prefix start.
        :param split_sentence: To look in.
        :param prefix: The prefix before the misspelled word.
        :return: The first index where the prefix starts.
        """
        if len(prefix) != 0:
            return split_sentence.index(prefix[0])
        else:
            return 0

