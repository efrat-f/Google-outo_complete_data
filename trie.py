from trie__node import TrieNode


class Trie():
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, string):
        node = self.__root
        for char in string:
            if node.get_child(char) is None:
                node.set_children(char)
            node = node.get_child(char)
        node.set_end()
