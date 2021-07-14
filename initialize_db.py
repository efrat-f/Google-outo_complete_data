import os

from trie import Trie


class Initialize_DB:
    def __init__(self):
        self.__root_directory = 'resources'
        self.__trie = Trie()

    def run(self):
        for (root, dirs, files) in os.walk(self.__root_directory, topdown=True):
            for file in files:
                with open(root + "\\" + file, encoding="utf8") as initialize_file:
                    for line in initialize_file:
                        self.__trie.insert(line)

