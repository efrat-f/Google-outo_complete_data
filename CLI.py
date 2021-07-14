import linecache

from initialize_db import Initialize_DB
from trie import Trie


class CLI:
    def __init__(self):
        self.__initialize_db = Initialize_DB()
        # self.__auto_implement = Auto_Implement()
        self.__trie = Trie()

    def get_from_file_by_offset(self, offset, file):
        return linecache.getline(file, offset+1)[:-2]

    def run(self):
        self.__initialize_db.run(self.__trie)
        print("Loading the files and preparing the system...")
        while True:
            node = None
            user_input = input("The system is ready. Enter your text:\n")
            user_request = user_input
            while user_request != "#":
                res, node = self.__trie.search(user_request, node)
                if res:
                    print("Here are 5 suggestions")
                    for i in range(len(res)):
                        print(f'{i}.{self.get_from_file_by_offset(res[i][0], res[i][1])}')
                else:
                    print("there are no results")
                    break
                user_request = input(user_input)
                user_input += user_request
