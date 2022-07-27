from AutoCompleteData import AutoCompleteData
from Data import Data
from Data import Sentence

def get_best_k_completions(prefix: str) -> list[AutoCompleteData]:
    results = []
    prefix = prefix.lower()
    user_search_list = prefix.split(" ")
    for id in data.get_data_word_to_sentence(user_search_list[0]):
        sentence = data.get_data_sentence_to_file(id)
        if len(results) == 5:
            break
        if sentence.get_sentence().lower().find(prefix) != -1:
            results.append(AutoCompleteData(prefix, sentence.get_sentence(), sentence.get_line(), 0, sentence.get_file_name()))
    return results

def print_user_input() -> None:
    user_search = input('Enter your text:')
    counter = 0
    for result in get_best_k_completions(user_search):
        counter+=1
        print(str(counter) + ". " + result.get_str())

data = Data()
print_user_input()