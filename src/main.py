import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')


class PasswordGeneratore(ABC):
    @abstractmethod
    def generate(self):
        """
        Abstract base class for generating passwords.
        """
        pass

class PinGenerator(PasswordGeneratore):
    """
    Class for generatting a random numeric PIN of given lenght.
    """
    def __init__(self, length: int):
        """
        Initalize the PinGenerator with a specified lenght for the PIN.

        :param lenght: The lenght of the PIN
        """
        self.length = length

    def generate(self):
        """
        Generats a random PIN consisting only of digits.

        :return: A random PIN as string.
        """
        return "".join([random.choice(string.digits) for _ in range(self.length)])

class RandomPassword(PasswordGeneratore):
    """
    Class for generating a random password with specified lenght and character types.
    """
    def __init__(self, length: int = 8, include_numbers: bool = True, include_symbols: bool = True):
        """
        Initilize the RandomPassword with given Parameters for password complexity.

        :param lenght: The lenght of the password (defult is 8).
        :param include_numbers: Whether to include numbers in the password (defult is True).
        :param include_symbols: Whether to include symbols in the password (defult is True).
        """
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        """
        Generates a arandom password with the specified properties.

        :return: a random passwprd as a string.
        """
        return "".join([random.choice(self.characters) for _ in range(self.length)])

class Memorablepassword(PasswordGeneratore):
    """
    Class for generating a memorable password consisting of random words.
    """
    def __init__(
            self,
            separator:str = "-",
            number_of_words: int = 8,
            capitalize: bool = False,
            vocabulary: list = None
    ):
        """
        Initializes the MemorablePassword with given properties for word-based password generation.

        :param seprator: The separator to use between words (defult is "-").
        :param number_of_words: The number of words to include in the password (defult is 4).
        :param capitalize: Whether to randomly capitalize words (defult is False).
        :param vocabulary: Custom vocabulary list, defult to the nltk words corpus.
        """
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.num_of_words = number_of_words
        self.separator = separator
        self.capitalize = capitalize

    def generate(self):
        """
        Generates a memorable password using random words.

        :return: A memorable password as a string.
        """
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]

        if self.capitalize:
            password_words = [words.upper() if random.choice((True, False))else words.lower() for words in password_words]

        return self.separator.join(password_words)

def main():
    print("Testing PinCodeGenerator:")
    test_pincode_generator()


def test_pincode_generator():
    pin_gen = PinGenerator(length=4)
    pin = pin_gen.generate()
    print(pin)
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)

if __name__ == "__main__":
    main()