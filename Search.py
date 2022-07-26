import AutoCompleteData
from Data import Data


def get_best_k_completions(prefix: str) -> list[AutoCompleteData]:
    results = []
    prefix = prefix.lower()
    user_search_list = prefix.split(" ")
    for sentence in data.get_data_word_to_sentence(user_search_list[0]):
        for result in sentence:
            kkk = data.get_data_sentence_to_file(results)
            if len(results) == 5:
                break
            if kkk.get_sentence().lower().find(prefix) != -1:
                results.append(AutoCompleteData(prefix, kkk.get_sentence(), kkk.get_line(), 0, kkk.get_file_name()))
    return results

def print_user_input() -> None:
    user_search = input('Enter your text:')
    counter = 1
    for result in get_best_k_completions(user_search):
        print(counter++ + '. ' + result)

data = Data()
print_user_input()