import Controller


def main():
    controller = Controller.Controller()

    prefix = "first lige"
    for i, completion in enumerate(controller.get_best_k_completions(prefix)):
        print(str(i) + '. ' + str(completion))


if __name__ == '__main__':
    main()
