# Custom Prefix Trie Implemented in Redis from Scratch for a Scalable Search Autocomplete System.  


Search autocomplete, like used with many companies such as Amazon, Google and Uber is an important feature of many products.  Here I implement it from scratch and represent the Trie in the Key-Value store Redis.  I then run the autocomplete live with a simple Flask application.  




![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png


### Brief Overview


In order to implement a scalable search autocomplete, we need the right data structures.  If our dataset is  small, we can just store all our words in a relational database and fetch them using simple SQL queries using the LIKE command.  In my case, I am trying to build a scalable trie, so this would be inefficent the larger our lookup database got.  The way around this is using a Trie, or Prefix Trie.  










