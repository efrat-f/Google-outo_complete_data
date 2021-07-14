from trie_node import TrieNode


class Trie:
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, string):
        node = self.__root
        for char in string:
            if node.get(char) is None:
                node.set(char)
            node = node.get(char)
        node.set_end()

