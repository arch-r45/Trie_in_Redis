import copy
class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False
class Trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True
    def autocomplete(self, prefix):
        res = set()
        node = self.root
        curr = ""
        for char in prefix:
            if char not in node.children:
                return None
            curr += char
            node = node.children[char]
        if node.word == True:
            res.add(curr)
        def dfs(cur, node):
            if node.word == True:
                res.add("".join(cur))
            if node == None:
                return
            for children in node.children:
                cur.append(children)
                dfs(cur, node.children[children])
                cur.pop()
        cur = list(curr)
        dfs(cur, node)
        return list(res)