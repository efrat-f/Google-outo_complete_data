import os

from trie import Trie


class Initialize_DB:
    def __init__(self):
        self.__root_directory = 'resources\\2021-archive\\python-3.8.4-docs-text\\c-api'

    def run(self, trie):
        for (root, dirs, files) in os.walk(self.__root_directory, topdown=True):
            for file in files:
                with open(root + "\\" + file, encoding="utf8") as initialize_file:
                    counter = 0
                    for line in initialize_file:
                        trie.insert_word(" ".join(line[:-2].split()), counter, root + "\\" + file)
                        counter += 1
        return trie

