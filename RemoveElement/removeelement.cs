using System;

namespace RemoveElement
{
    public class Solution 
    {
        public int RemoveElement(int[] nums, int val) 
        {
            if (nums.Length == 0 || nums.Length > 100 || val < 0 || val > 50)
            {
                return 0;
            }

            int count = 0;

            foreach (int num in nums)
            {
                if (num == val)
                {
                    continue;
                }
                
                nums[count] = num;
                count++;
            }

            return count;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            int[] nums1 = {3, 2, 2, 3};
            int val1 = 3;
            int[] nums2 = {0, 1, 2, 2, 3, 0, 4, 2};
            int val2 = 2;

            Solution test = new Solution();

            Console.WriteLine("Example 1: " + test.RemoveElement(nums1, val1));
            Console.WriteLine("Example 2: " + test.RemoveElement(nums2, val2));
        }
    }
}
