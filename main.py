import Clean_line
import Controller


def main():
    controller = Controller.Controller()

    print("Please insert your input...")
    prefix = Clean_line.clean_line_from_redundant_letters(input())

    while prefix != "finish":
        for i, completion in enumerate(controller.get_best_k_completions(prefix)):
            print(str(i) + '. ' + str(completion))
        print("Please insert your input...")
        prefix = Clean_line.clean_line_from_redundant_letters(input())

    print("By")


if __name__ == '__main__':
    main()
