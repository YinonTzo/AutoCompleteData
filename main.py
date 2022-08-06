
import Search


def main():
    prefix = "line in"
    for i, completion in enumerate(Search.get_best_k_completions(prefix)):
        print(str(i) + '. ' + str(completion))


if __name__ == '__main__':
    main()
