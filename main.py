import Clean_line
import Controller


def main():
    controller = Controller.Controller()

    prefix = Clean_line.clean_line_from_redundant_letters(input())
    for i, completion in enumerate(controller.get_best_k_completions(prefix)):
        print(str(i) + '. ' + str(completion))


if __name__ == '__main__':
    main()
