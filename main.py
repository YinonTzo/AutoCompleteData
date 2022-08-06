from Data import Data
import Search

if __name__ == '__main__':
    prefix = "line in"
    misspelled_words_counter, misspelled_word, intersection_of_lines = Search.find_perfect_match(prefix)
    if misspelled_words_counter == 0:
        for res in Search.find_complete_sentence(prefix, intersection_of_lines):
            print(res)

    # elif misspelled_words_counter == 1:
    #     Search.try_to_fix_word(prefix, misspelled_word, intersection_of_lines)


    #print_user_input()