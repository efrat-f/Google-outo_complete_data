from string import ascii_lowercase

from trie import Trie


class CLI:
    def __init__(self):
        self.__trie = Trie()

    def run(self):
        # print("Loading the files and preparing the system...")
        # user_input = input("The system is ready. Enter your text:")
        # while user_input != "#":
        #     res, node = self.__trie.search(user_input)
        #     for search in res:
        pass

    def manipulation_switching(self, string):
        for i in range(len(string) - 4):
            for char in ascii_lowercase:
                string[i] = char
                self.__trie.search(string)
