import Clean_line
from Data import Data
from AutoCompleteData import AutoCompleteData


class CompleteSentenceSearcher:
    """A CompleteSentenceSearcher class. If all word in the user input exists,
    the searcher will make search of the complete sentence in the intersection of lines.

    Args:
        data (Data): The database.
    """
    def __init__(self, data: Data):
        self.__data = data

    def find_complete_sentence(self, prefix: str, intersection_of_lines: set[int]) -> list[AutoCompleteData]:
        """
        Go over all sentences in the intersection and check for every sentence if the user input
        exist.
        :param prefix: The user input.
        :param intersection_of_lines: The lines in database where all words from the user input exist
        there.
        :return: A list of AutoCompleteData.
        """
        results = list()
        for line in intersection_of_lines:
            offset = (Clean_line.clean_line_from_redundant_letters(self.__data.get_sentence_to_file(line)
                      .sentence)).find(prefix)
            if offset != -1:
                results.append(AutoCompleteData(
                    self.__data.get_sentence_to_file(line).sentence,
                    self.__data.get_sentence_to_file(line).file_name,
                    self.__data.get_sentence_to_file(line).line_number,
                    len(prefix)))
        return results


