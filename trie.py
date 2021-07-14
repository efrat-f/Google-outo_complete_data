from db_dict_alpha import DBDictAlpha
from trie_node import TrieNode


class Trie:
    def __init__(self):
        self.__root = TrieNode()
        self.__dict_alpha = DBDictAlpha()

    def insert(self, string, offset, file):
        node = self.__root
        for char in string:
            if not 96 < ord(char) < 123 and not 64 < ord(char) < 91 and not char == " ":
                continue
            char = char.lower()
            if node.get(char) is None:
                node.add_child(char)
            node = node.get(char)
        if node.get(chr(97 + 27)) is None:
            node.add_child(chr(97 + 27), [])
        node = node.get(chr(97 + 27))
        node.add_end((offset, file))

    def search(self, string, root=None):
        results = []
        if root is None:
            root = self.__root
        node = root
        for char in string:
            if not 96 < ord(char) < 123 and not 64 < ord(char) < 91 and not char == " ":
                continue
            char = char.lower()
            node = node.get(char)
            if node is None:
                return results, node
        results = node.dfs(results)
        return results, node

    def insert_word(self, string, offset, file):
        for i in range(len(string)):
            self.insert(string[i:], offset, file)
