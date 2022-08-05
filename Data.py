import os


class Sentence:
    def __init__(self, sentence, file_name):
        self.sentence = sentence
        self.file_name = file_name

    def get_sentence(self):
        return self.sentence

    def get_file_name(self):
        return self.file_name

    def get_line(self):
        return self.line


class Data:

    def __init__(self):
        """
        Read all the files from the Resources.
        :return:A dictionary which each key is a word inside a file,
        and for each word a list of number of lines where contain this word.
        """
        self.word_to_sentence = dict()
        self.sentence_to_file = list()
        for root, dirs, files in os.walk('stam'):
            for file in files:  # get each file within the directory and subdirectories
                path = (os.path.abspath(os.path.join(root, file)))  # get the full path of each file
                with open(path, encoding="utf8") as f:  # open the file
                    for line in f:
                        self.sentence_to_file.append(Sentence(line[:-1], file[:-4]))
                        for word in line.replace('\n', "").split(" "):  # every word separated by space
                            word = word.lower()
                            if word not in self.word_to_sentence:
                                self.word_to_sentence[word] = set()
                            self.word_to_sentence[word].add(len(self.sentence_to_file)-1)  # add the line to the key word

    def get_data_word_to_sentence(self, word) -> set[int]:
        if word not in self.word_to_sentence.keys():
            return set()
        return self.word_to_sentence[word]

    def get_data_sentence_to_file(self, index) -> Sentence:
        return self.sentence_to_file[index]
