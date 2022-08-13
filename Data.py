import os
import Sentence


class Data:
    """
    A Data class. Keep the data from Archive.

    Attributes:
        word_to_sentence (dict): Map word to its sentence.
        sentence_to_file (list): Save the sentences.
    """

    def __init__(self):
        self.__word_to_sentence = dict()
        self.__sentence_to_file = list()
        for root, dirs, files in os.walk('stam'):
            for file in files:  # get each file within the directory and subdirectories
                path = (os.path.abspath(os.path.join(root, file)))  # get the full path of each file
                with open(path, encoding="utf8") as f:  # open the file
                    for line in f:
                        self.__sentence_to_file.append(Sentence.Sentence(line.replace('\n', ""), file[:-4]))
                        for word in line.replace('\n', "").split(" "):  # every word separated by space
                            word = word.lower()
                            if word not in self.__word_to_sentence:
                                self.__word_to_sentence[word] = set()
                            self.__word_to_sentence[word].add(
                                len(self.__sentence_to_file) - 1)  # add the line to the key word

    def get_lines_from_word_to_sentence(self, word: str) -> set[int] | None:
        """
        Check if the word exists, return the sentence that it belong.
        :param word: Word from sentence.
        :return: A set of sentences that this word exists.
        """
        if word not in self.__word_to_sentence:
            return None
        return self.__word_to_sentence[word]

    def get_sentence_to_file(self, index) -> Sentence:
        """
        Return the complete sentence.
        :param index: Where the sentence exists.
        :return: A Sentence from the list.
        """
        return self.__sentence_to_file[index]
