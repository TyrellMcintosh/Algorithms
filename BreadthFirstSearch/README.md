### Binary Tree Level Order Traversal
<p>Instructions: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level). </p>

### Approach
<p> Very efficient algorithm that utlizes more memory to improve on performance </p>

* Use a queue to add the root and its children
* Keep track of depth and num of nodes left on that level
* If there are no more nodes on the level, and theres still nodes (children) in the queue:
	* a new level is reached so we increase depth
	* set the number of nodes to that level
	* create a new list for those nodes to be output to


### Concepts Used 
* Binary Tree
* Breadth-First Search
* Tree

#

### Performance
#### Runtime
**141 ms** faster than **98.20%** of C# online submissions.

#### Memory Usage
**43.1 MB** less than **12.90%** of C# online submissions.

#### Test Cases
**34/34** test cases passed.
