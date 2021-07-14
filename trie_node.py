class TrieNode:
    alphabet_size = 64

    # Trie node class
    def __init__(self, end=False):
        self.__children = [None] * type(self).alphabet_size
        # isEndOfWord is True if node represent the end of the word
        self.__is_end = end

    def set(self, chr, val):
        self.__children[ord(chr) - 97] = val

    def get(self, chr):
        return self.__children[ord(chr) - 97]

    def get_end(self):
        return self.__is_end

    def set_end(self, val):
        self.__is_end = val

    def add_child(self, chr, end=False):
        node = TrieNode(end)
        self.set_child(chr, node)

    def dfs(self, arr_completes):
        while len(arr_completes) < 5:
            if self.get_end():
                if self.get_end() not in arr_completes:
                    arr_completes.append(self.get_end())
                return
            for i in self.__children:
                if i is not None:
                    i.dfs(arr_completes)
            return arr_completes
