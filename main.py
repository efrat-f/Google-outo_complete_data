from CLI import CLI
from trie import Trie

# for i in range(65, 90):
#     print(chr(i))
# print(chr(321).isalpha())
# #
# trie = Trie()
# trie.insert_word("bc", 1, 2)
# trie.insert_word("abcsab", 1, 2)
# trie.insert_word("abcsaa", 1, 2)
# trie.insert_word("acdab", 1, 2)
# trie.insert_word("acda", 1, 2)
# print(trie.switching_manipulation("abcsad"))

cli = CLI()
cli.switching_manipulation()
