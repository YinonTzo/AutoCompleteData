import Controller


def main():
    controller = Controller.Controller()

    # prefix = "second lige"
    prefix = "first line"
    for i, completion in enumerate(controller.get_best_k_completions(prefix)):
        print(str(i) + '. ' + str(completion))


if __name__ == '__main__':
    main()
