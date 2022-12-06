### Valid Palindrome
<p>Instructions: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
  removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include 
  letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise. </p>

### Approach
<p> Pretty efficient on performance. </p>

* Convert the string into a list of characters.
* Make every character lowercase for the equality check.
* Check if length is an even or odd number to find the middle number.
* Compare the first and last character then increment i each time.


### Concepts Used 
* Two Pointers
* String

#

### Performance
#### Runtime
**78 ms** faster than **96.42%** of C# online submissions.

#### Memory Usage
**40.7 MB** less than **36.10%** of C# online submissions.

#### Test Cases
**404/404** test cases passed.
