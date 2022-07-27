from AutoCompleteData import AutoCompleteData
from Data import Data
from Data import Sentence

mistake_word =""

def get_best_k_completions(prefix: str) -> list[AutoCompleteData]:
    results = []
    mistake_word = []
    prefix = prefix.lower()
    user_search_list = prefix.split(" ")
    #for id in data.get_data_word_to_sentence(user_search_list[0]):
    for id in make_intersection(user_search_list):
        sentence = data.get_data_sentence_to_file(id)
        if len(results) == 5:
            break
        if sentence.get_sentence().lower().find(prefix) != -1:
            results.append(AutoCompleteData(prefix, sentence.get_sentence(), sentence.get_line(), 0, sentence.get_file_name()))
    return results

"""
get a senence 
"""
def make_intersection(list_words: list[str]) -> set[int]:
    mistake_words = 0
    mistake_in_word =""
    set_intersection = data.get_data_word_to_sentence(list_words[0])
    for word in list_words:
        sentences = data.get_data_word_to_sentence(word)
        if len(sentences) == 0:
            mistake_words+=1
            if mistake_words > 1:
                return set()
        set_intersection = set_intersection.intersection(sentences)
    return set_intersection

def print_user_input() -> None:
    user_search = input('Enter your text:')
    counter = 0
    for result in get_best_k_completions(user_search):
        counter+=1
        print(str(counter) + ". " + result.get_str())

data = Data()
print_user_input()