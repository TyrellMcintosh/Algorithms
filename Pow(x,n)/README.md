### Pow(x, n)
<p>Instructions: Implement pow(x, n), which calculates x raised to the power n (i.e., xn). </p>

### Approach
<p> A recursive approach would have better performance however I believed this approach to be easier to understand. </p>

* If the base number is either 0, 1 or -1 we return that number since 0ⁿ = 0, 1ⁿ = 1 and -1ⁿ = -1
* If the exponent is 0 we return 1, if -1 we return its reciprocal
* If exponent is negative we convert to a positive and use a boolean as a flag to indicate it was a negative
* Use a loop to multiple the base number by itself
* Return the product if the flag is false, if true we return 1/product


### Concepts Used 
* Math

#

### Performance
#### Runtime
**44 ms** faster than **46.61%** of C# online submissions.

#### Memory Usage
**25.4 MB** less than **70.19%** of C# online submissions.

#### Test Cases
**305/305** test cases passed.
