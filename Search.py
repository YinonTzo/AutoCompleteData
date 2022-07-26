import AutoCompleteData
import Data

def get_best_k_completions(prefix: str) -> list[AutoCompleteData]:
    results = []
    data = get_data()
    prefix = prefix.lower()
    user_search_list = prefix.split(" ")
    for result in data[user_search_list[0]]:
        if result[0].lower().find(prefix) != -1:
            results.append(AutoCompleteData(prefix, result[0], result[1], 0, result[2]))
            if len(results) == 5:
                break
    return results

def print_user_input() -> None:
    user_search = input('Enter your text:')
    counter = 1
    for result in get_best_k_completions(user_search):
        print(counter++ + '. ' + result)

print_user_input()