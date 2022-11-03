#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n < 4)
            return n;

        vector<int> dp(n+1);
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];       
    }
};

int main() {
    int n1 = 1;
    int n2 = 2;
    int n3 = 3;
    int n4 = 4;
    int n5 = 5;
    int n6 = 6;
    
    Solution test;

    cout << "Example 1: " << test.climbStairs(n1);
    cout << "\nExample 2: " << test.climbStairs(n2);
    cout << "\nExample 3: " << test.climbStairs(n3);
    cout << "\nExample 4: " << test.climbStairs(n4);
    cout << "\nExample 5: " << test.climbStairs(n5);
    cout << "\nExample 6: " << test.climbStairs(n6);

    return 0;
}
