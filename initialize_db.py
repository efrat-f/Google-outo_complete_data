from trie import Trie


class Initialize_DB:
    def __init__(self):
        self.__file_name = 'file.txt'
        self.__trie = Trie()

    def run(self):
        try:
            with open(self.__file_name, "r") as file:
                offset = 0
                for line in file:
                    self.__trie.insert(line, self.__file_name, offset)
                    offset += 1
        except:
            pass


