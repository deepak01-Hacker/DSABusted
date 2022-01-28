class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for s in word:
            if s not in node.child:
                node.child[s] = TrieNode()
            node = node.child[s]
        node.val = word

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def match(word, depth, node):
            if depth == len(word): return not (node.val=='')
            if word[depth] != '.':
                return word[depth] in node.child and match(word, depth + 1, node.child[word[depth]])
            else:
                for c in node.child:
                    if match(word, depth+1, node.child[c]):
                        return True
            return False
        return match(word, 0, self.root)

class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.val = ""


