from typing import Tuple, Set, Any

from AutoCompleteData import AutoCompleteData
import Data
import Sentence


class Searcher:

    def __init__(self):
        self.data = Data.Data()

    def get_best_k_completions(self, prefix: str) -> list[AutoCompleteData]:
        misspelled_words_counter, misspelled_word, misspelled_word_place, \
            intersection_of_lines, = self.find_perfect_match(prefix)

        if misspelled_words_counter == 0:
            return self.find_complete_sentence(prefix, intersection_of_lines)[:5]
        elif misspelled_words_counter == 1:
            return self.find_real_word(prefix, misspelled_word, misspelled_word_place, intersection_of_lines)

    def find_perfect_match(self, prefix: str) -> tuple[int, str, int, set[int]]:
        intersection_of_lines = set()
        misspelled_words_counter = 0
        misspelled_word_place = 0
        misspelled_word = ''

        prefix_list = prefix.lower().split(" ")
        for i, word in enumerate(prefix_list):
            numbers_of_lines = self.data.get_data_word_to_sentence(word)
            if numbers_of_lines:
                intersection_of_lines = self.make_intersection(intersection_of_lines, numbers_of_lines)
            else:
                misspelled_word_place = i
                misspelled_words_counter += 1
                misspelled_word = word

        return misspelled_words_counter, misspelled_word, misspelled_word_place, intersection_of_lines

    def make_intersection(self, intersection_of_lines: set[int], numbers_of_lines: set[int]) -> set[int]:
        if intersection_of_lines:
            intersection_of_lines = intersection_of_lines.intersection(numbers_of_lines)
        else:
            intersection_of_lines = numbers_of_lines
        return intersection_of_lines

    def find_complete_sentence(self, prefix: str, intersection_of_lines: set[int]) -> list[AutoCompleteData]:
        results = list()
        for line in intersection_of_lines:
            offset = self.data.get_data_sentence_to_file(line).get_sentence().find(prefix)
            if offset != -1:
                results.append(AutoCompleteData(
                    self.data.get_data_sentence_to_file(line).get_sentence(),
                    self.data.get_data_sentence_to_file(line).get_file_name(),
                    offset, 0))
        return results

    def find_real_word(self, user_input, misspelled_word, misspelled_word_place, intersection_of_lines):
        split_user_input = user_input.split(" ")
        prefix = split_user_input[:misspelled_word_place]
        suffix = split_user_input[misspelled_word_place + 1:]

        fix_sentences = list()
        for line in intersection_of_lines:
            split_sentence = self.data.get_data_sentence_to_file(line).get_sentence().split(" ")

            first_match_index = split_sentence.index(prefix[0])
            real_word_index = first_match_index + len(prefix)

            if self.check_pattern_match(first_match_index, split_sentence, prefix) and \
                    self.check_pattern_match(real_word_index + 1, split_sentence, suffix):
                if self.fix_word(misspelled_word, split_sentence[real_word_index]):
                    fix_sentences.append(AutoCompleteData(
                        self.data.get_data_sentence_to_file(line).get_sentence(),
                        self.data.get_data_sentence_to_file(line).get_file_name(),
                        0, 0))
                elif len(suffix) == 0:  # it means that all the words are ok but the last.
                    return self.find_complete_sentence(user_input, intersection_of_lines)[:5]

        return fix_sentences[:5]

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
