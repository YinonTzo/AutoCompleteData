class DeleteLetter:

    @staticmethod
    def fix_by_delete_letter(self, misspelled_word, real_word):
        for i in range(0, len(misspelled_word)):
            if misspelled_word[:i] + misspelled_word[i + 1:] == real_word:
                return i
        return -1
