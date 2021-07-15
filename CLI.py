from string import ascii_lowercase
import linecache


from initialize_db import Initialize_DB
from trie import Trie


class CLI:
    def __init__(self):
        self.__trie = Trie()
        self.__initialize_db = Initialize_DB()

    def get_from_file_by_offset(self, offset, file):
        return linecache.getline(file, offset+1)[:-2]

    def run(self):
        self.__initialize_db.run(self.__trie)
        print("Loading the files and preparing the system...")
        self.__initialize_db.run(self.__trie)
        while True:
            node = None
            user_input = input("The system is ready. Enter your text:\n")
            user_request = user_input
            node = None
            while user_request != "#":
                res, node = self.__trie.search(user_request, node)
                if res:
                    print("Here are 5 suggestions")
                    for i in range(len(res)):
                        print(f'{i + 1}.{res[i]}')
                else:
                    print("query doe's not exit")
                    break
                user_request = input(user_input + " ")
                user_input += user_request

    def switching_manipulation(self):
        self.__initialize_db.run(self.__trie)
        while True:
            user_input = input("The system is ready. Enter your text:\n")
            user_request = user_input
            node = None
            while user_request != "#":
                for i in range(4, len(user_request)):
                    for letter in ascii_lowercase:
                        temp_request = user_request[:i+1] + letter + user_request[i+2:]
                        res, node = self.__trie.search(temp_request, node)
                        if res:
                            print("Here are 5 suggestions")
                            for i in range(len(res)):
                                print(f'{i + 1}.{res[i]}')
                user_request = input(user_input + " ")
                        print(f'{i}.{self.get_from_file_by_offset(res[i][0], res[i][1])}')
                else:
                    print("there are no results")
                    break
                user_request = input(user_input)
                user_input += user_request
