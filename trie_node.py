class TrieNode:
    alphabet_size = 29

    # Trie node class
    def __init__(self, end=False):
        self.__children = [None] * type(self).alphabet_size
        # isEndOfWord is True if node represent the end of the word
        self.__is_end = end

    def set(self, chr, val):
        if chr == " ":
            self.__children[28] = val
            return
        self.__children[ord(chr) - 97] = val

    def get(self, chr):
        if chr == " ":
            return self.__children[28]
        return self.__children[ord(chr) - 97]

    def get_end(self):
        return self.__is_end

    def set_end(self, val):
        self.__is_end = val

    def add_child(self, chr, end=False):
        node = TrieNode(end)
        self.set(chr, node)

    def dfs(self, arr_completes):
        if self.get_end():
            for complete in self.get_end():
                if len(arr_completes) >= 5:
                    return
                exist = False
                for obj in arr_completes:
                    if obj[0] == complete[0] and obj[1] == complete[1]:
                        exist = True
                        break
                if not exist:
                    arr_completes.append(complete)
            return
        for i in self.__children:
            if i is not None:
                i.dfs(arr_completes)
        return arr_completes

    def add_end(self, auto_complete):
        self.__is_end.append(auto_complete)
