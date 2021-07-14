from trie__node import TrieNode


class Trie():
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, string):
        node = self.__root
        for char in string:
            if node.containsKey(char) is None:
                node.put(char)
            node = node.get(char)
        node.set_end()
