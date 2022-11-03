#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        
        int end = nums.size()-1;
        
        for (int i = nums.size() - 2; i >= 0; i--)   // Iterate backwards at 2nd last pos
        {
            if (i + nums[i] >= end)  // sum of the index and element is max distance can jump
                end = i;    // new distance to reach
        }
        
        if (end == 0) 
            return true;
        
        return false;
    }
};    

int main() {
    vector<int> nums1 = {2, 3, 1, 1, 4};
    vector<int> nums2 = {3, 2, 1, 0, 4};
        
    Solution test;
    
    cout << "Example 1: " << test.canJump(nums1);
    cout << "Example 2: " << test.canJump(nums2);
        
    return 0;
}
