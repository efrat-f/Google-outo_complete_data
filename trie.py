from db_dict_alpha import DBDictAlpha
from trie_node import TrieNode


class Trie:
    def __init__(self):
        self.__root = TrieNode()
        self.__dict_alpha = DBDictAlpha()

    def insert(self, string):
        node = self.__root
        for char in string:
            if not 97 <= ord(char) < 123:
                continue
            char = char.lower()
            if node.get(char) is None:
                node.add_child(char)
                node = node.get(char)
                self.__dict_alpha.add_item(char, node)
            else:
                node = node.get(char)
        node.add_child(chr(97+27), string)

    def search(self, string):
        results = []
        for start in self.__dict_alpha.get_item(string[0]):
            node = start
            for char in string[1:]:
                node = node.get_child(char)
                if node is None:
                    return None
            node.dfs(results)
        return results