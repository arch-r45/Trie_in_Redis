import redis
import redis_.trie_class 
r = redis.Redis(host='localhost', port=6380, decode_responses=True)
def populate_trie(file_path):
    trie = redis_.trie_class.Trie()
    with open(file_path, 'r', newline='') as file:
        for row in file:
            k_v_list = row.split(",")
            node = k_v_list[0]
            trie.insert(node)
        return trie
"""
Below we are going to load the trie into Redis.  This can be done generating all substrings that come before
the word.  Once you have a substring, you call the method "autocomplete" and store the k most frequent words
for that substring.  
In this case, because we have a static amount of words that are never changing, and we never need to live 
update these as an application like twitter would need to, we can just sort the words based on 
lexicographic order and return the top k elements.  Obviously in other applications, here is where you may
return the top k "most frequent" words.  However there is only about 2000 words in my dataset so no need.
"""
def load_trie(trie, k):
    def dfs(node, curr):
        if node.children == None:
            return
        for children in node.children:
            curr.append(children)
            suggestions = trie.autocomplete("".join(curr))
            suggestions = sorted(suggestions)[:k]
            print(suggestions)
            r.rpush("".join(curr), *suggestions)
            dfs(node.children[children], curr)
            curr.pop()
    dfs(trie.root, [])


file_path = "Shakespeare_glossary_dict.csv"
k = 3
trie_object = populate_trie(file_path)
load_trie(trie_object, k)















    


    
















