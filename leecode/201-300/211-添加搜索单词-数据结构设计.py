class TreeNode:
    def __init__(self, val):
        self.val = val
        self.end = False
        self.children = []


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode('')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.addhelper(self.root, word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the
        dot character '.' to represent any one letter.
        """
        return self.searchhelper(self.root, word)

    def addhelper(self, root, word):
        if word == '':
            root.end = True
            return
        for cur in root.children:
            if word[0] == cur.val:
                self.addhelper(cur, word[1:])
                return
        cur = TreeNode(word[0])
        root.children.append(cur)
        self.addhelper(cur, word[1:])

    def searchhelper(self, root, word):
        if word == '':
            return root.end
        if word[0] == '.':
            for cur in root.children:
                if self.searchhelper(cur, word[1:]):
                    return True
        else:
            for cur in root.children:
                if word[0] == cur.val:
                    return self.searchhelper(cur, word[1:])
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
