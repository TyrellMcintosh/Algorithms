### Gas Station
<p>Instructions: There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique. </p>

### Approach
<p> Could have improved on performance however this route is easier to understand </p>

* Check if fuel exceeds the cost
	* If yes, you can travel 
	* If no, you can't travel so return -1 
* Add current fuel and subtract the cost
	* If cost exceeds fuel you set the return value to current index and reset the fuel
	* If you can continue to add fuel and subtract cost then you return that index


### Concepts Used 
* Greedy
* Array

#

### Performance
#### Runtime
**417 ms** faster than **29.02%** of C# online submissions.

#### Memory Usage
**47.4 MB** less than **29.80%** of C# online submissions.

#### Test Cases
**37/37** test cases passed.
