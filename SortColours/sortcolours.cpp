#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int temp = 0;
        
        while(temp != -1)
        {
            temp = -1;

            for (int i = 0; i < nums.size() - 1; i++)
            {
                if (nums[i+1] < nums[i])
                {
                    temp = nums[i+1];
                    nums[i+1] = nums[i];
                    nums[i] = temp;
                }
            }
        }      
    }
};

int main() {
    vector<int> nums1 = {2, 0, 2, 1, 1, 0};
    vector<int> nums2 = {2, 0, 1};

    Solution test;

    test.sortColors(nums1);
    test.sortColors(nums2);

    return 0;
}
