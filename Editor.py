from Data import Data
from AutoCompleteData import AutoCompleteData
import CompleteSentenceSearcher
import MisspelledWordDetails


class Editor:
    """

    Args:


    Attributes:

    """
    def __init__(self, data: Data, complete_sentence_searcher: CompleteSentenceSearcher):
        self.data = data
        self.complete_sentence_searcher = complete_sentence_searcher

    def find_real_word(self, user_input: str,
                       misspelled_word: MisspelledWordDetails,
                       intersection_of_lines: set[int]) -> list[AutoCompleteData]:

        split_user_input = user_input.split(" ")
        prefix = split_user_input[:misspelled_word.misspelled_word_place]
        suffix = split_user_input[misspelled_word.misspelled_word_place + 1:]

        fixed_sentences = list()
        for line in intersection_of_lines:
            split_sentence = self.data.get_sentence_to_file(line).sentence.split(" ")

            if len(prefix) != 0:
                first_match_index = split_sentence.index(prefix[0])
            else:
                first_match_index = 0
            real_word_index = first_match_index + len(prefix)

            if self.check_pattern_match(first_match_index, split_sentence, prefix) and \
                    self.check_pattern_match(real_word_index + 1, split_sentence, suffix):
                if self.fix_word(misspelled_word.misspelled_word, split_sentence[real_word_index]):
                    fixed_sentences.append(AutoCompleteData(
                        self.data.get_sentence_to_file(line).sentence,
                        self.data.get_sentence_to_file(line).file_name,
                        0, 0))
                elif len(suffix) == 0:  # it means that all the words are ok but the last.
                    return self.complete_sentence_searcher.find_complete_sentence(user_input, intersection_of_lines)

        return fixed_sentences

    def check_pattern_match(self, index, complete_sentence, partial_input):
        if len(partial_input) > len(complete_sentence[index:]):
            return False
        if len(partial_input) == 0:
            return True

        for i in range(0, len(partial_input)):
            if complete_sentence[index + i] != partial_input[i]:
                return False
        return True

    def fix_word(self, misspelled_word, real_word):
        if self.fix_by_delete_letter(misspelled_word, real_word):
            print("delete word")
            return True
        if self.fix_by_add_letter(misspelled_word, real_word):
            print("add word")
            return True
        if self.fix_by_change_letter(misspelled_word, real_word):
            print("change word")
            return True

    def fix_by_delete_letter(self, misspelled_word, real_word):
        for i in range(0, len(misspelled_word)):
            if misspelled_word[:i] + misspelled_word[i + 1:] == real_word:
                return True
        return False

    def fix_by_add_letter(self, misspelled_word, real_word):
        return self.fix_by_delete_letter(real_word, misspelled_word)

    def fix_by_change_letter(self, misspelled_word, real_word):
        for i in range(0, len(misspelled_word)):
            if misspelled_word[:i] == real_word[:i] and \
                    misspelled_word[i + 1:] == real_word[i + 1:]:
                return True
        return False