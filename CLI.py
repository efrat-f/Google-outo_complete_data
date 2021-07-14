from initialize_db import Initialize_DB
from trie import Trie


class CLI:
    def __init__(self):
        self.__trie = Trie()


    def run(self):
        self.__initialize_db.run(self.__trie)
        node = None
        print("Loading the files and preparing the system...")
        while True:
            user_input = input("The system is ready. Enter your text:\n")
            user_request = user_input
            while user_request != "#":
                res, node = self.__trie.search(user_request, node)
                if res:
                    print("Here are 5 suggestions")
                    for i in range(len(res)):
                        print(f'{i}.{res[i]}')
                user_request = input(user_input + " ")
                user_input += user_request
