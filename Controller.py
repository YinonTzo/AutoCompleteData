import AutoCompleteData
import Data
import CompleteSentenceSearcher
import IntersectionMaker
import Editor


class Controller:
    """
    Controller class. Manage the whole process.

    Attributes:
        data (Data): The database.
        intersection_maker (IntersectionMaker): Responsible on the first step in the algorithm.
        complete_sentence_searcher (CompleteSentenceSearcher): If there isn't misspelled word,
        this object will look for the sentence in the lines that returned from intersection maker.
        editor (Editor): If there is one mistake, this object will try to fix it and look for
        fits completions.
    """

    def __init__(self):
        self.__data = Data.Data()
        self.__intersection_maker = IntersectionMaker.IntersectionMaker(self.__data)
        self.__complete_sentence_searcher = CompleteSentenceSearcher.CompleteSentenceSearcher(self.__data)
        self.__editor = Editor.Editor(self.__data, self.__complete_sentence_searcher)

    def get_best_k_completions(self, prefix: str) -> list[AutoCompleteData] | str:
        """
        Check if there are 0, 1 or more misspelled words and
        return the answers to user.
        :param prefix: The user input.
        :return: If there isn't error, it will return the 5 first completions.
        If there is one error, it will return the five highest scored.
        If there are more than 1 error, it will return error message.
        """
        misspelled_words, intersection_of_lines = self.__intersection_maker.find_intersections(prefix)

        if len(misspelled_words) == 0:
            return self.__complete_sentence_searcher.find_complete_sentence(prefix,
                                                                            intersection_of_lines)[:5]
        elif len(misspelled_words) == 1:
            return self.__editor.find_real_word(prefix,
                                                misspelled_words[0],
                                                intersection_of_lines)[:5]
        else:
            return "Only one mistake is allowed"
