import string


def remove_punctuation(sentence: str) -> str:
    """
    https://datagy.io/python-remove-punctuation-from-string/
    Remove all punctuations from sentence
    :param sentence: To clean from punctuation.
    :return: New sentence without punctuation.
    """
    return sentence.translate(str.maketrans('', '', string.punctuation))


def remove_redundant_spaces(sentence: str):
    """
    https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string
    Remove multiple space from sentence.
    :param sentence: To clean from redundant spaces.
    :return: New sentence without redundant spaces.
    """
    return " ".join(sentence.split())


def clean_line_from_redundant_letters(sentence: str):
    """
    Remove redundant spaces and remove all punctuation from sentence.
    :param sentence: To clean.
    :return: New sentence as lower and clean.
    """
    return (remove_punctuation(remove_redundant_spaces(sentence))).lower()
