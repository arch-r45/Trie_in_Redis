# Custom Prefix Trie Implemented in Redis from Scratch for a Scalable Search Autocomplete System.  


Search autocomplete, like used with many companies such as Amazon, Google and Uber is an important feature of many products.  Here I implement it from scratch and represent the Trie in the Key-Value store Redis.  I then run the autocomplete live with a simple Flask application.  




![alt text][logo]

[logo]: https://github.com/arch-r45/Implementing-Trie-in-Redis-for-Fast-Prefix-Lookups--Glossary/blob/main/pictures/Google%20Search%20Picture.png


### Brief Overview


In order to implement a scalable search autocomplete, we need the right data structures.  If our dataset is  small, we can just store all our words in a relational database and fetch them using simple SQL queries using the LIKE command.  

```sql
SELECT * FROM "words"
WHERE query Like '%prefix'
LIMIT 3
```

In my case, I am trying to build a scalable trie, so this would be inefficent the larger our lookup database got.  The way around this is using a trie.  The trie offers 0(1) lookups for prefix search, meaning we can grab all the words very quickly and efficiently.  In my case I am also returning the top 3 sorted words.  In other cases, more complicated search autocomplete suggestions can be contrived. We could store the frequency of how many times each word has been searched, or use some type of Machine Learning model to predict the most likely search for a given user.  However, in this case, I am just returning the top 3 in any order



### Trie Implementation

I have implemented the Trie that we will be using from scratch in my application code.  The two main methods I implemented are the insert and autocomplete methods.  

```python
Trie.insert(word)
Trie.autocomplete(prefix)
```

Trie.insert is how we are going to load values into our trie, breaking up each word into syllables at each level of the tree.  When we call Trie.autocomplete() on any prefix, because the syllables are stored as keys to hashmaps, we can efficiently locate the correct prefix path.  Once we have the correct path, we can run a Depth First Search and return all the suggestions from a given prefix.  
















