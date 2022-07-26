import os


class Sentence:
    sentence: str
    file_name: str
    line: int


class Data:
    word_to_sentence: dict[set[int]]
    sentence_to_file: list[Sentence]

    def __init__(self):
        """
        Read all the files from the Resources.
        :return:A dictionary which each key is a word inside a file,
        and for each word a list of number of lines where contain this word.
        """
        word_to_sentence = {}
        sentence_to_file = list(list())
        for root, dirs, files in os.walk('Archive'):
            for file in files:  # get each file within the directory and subdirectories
                path = (os.path.abspath(os.path.join(root, file)))  # get the full path of each file
                with open(path, encoding="utf8") as f:  # open the file
                    line_num = 0
                    for line in f:
                        line_num += 1
                        sentence_to_file.append([line, file[:-4], line_num])
                        for word in line.split(" "):  # every word separated by space
                            word = word.lower()
                            if word not in word_to_sentence.keys():
                                word_to_sentence[word] = set()
                            word_to_sentence[word].add(line)  # add the line to the key word