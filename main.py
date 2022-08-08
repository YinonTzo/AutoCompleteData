
import Searcher


def main():
    searcher = Searcher.Searcher()

    prefix = "first lime"
    for i, completion in enumerate(searcher.get_best_k_completions(prefix)):
        print(str(i) + '. ' + str(completion))


if __name__ == '__main__':
    main()
