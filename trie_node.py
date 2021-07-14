class TrieNode:
    alphabet_size = 27

    # Trie node class
    def __init__(self):
        self.__children = [None] * type(self).alphabet_size
        # isEndOfWord is True if node represent the end of the word
        self.__is_end = False

    def set(self, chr, val):
        self.__children[ord(chr) - 97] = val

    def get(self, chr):
        return self.__children[ord(chr) - 97]

    def get_is_end(self):
        return self.__is_end

    def set_is_end(self, val):
        self.__is_end = val
