using System;

namespace RainWater
{
    public class Solution
    {
        public int Trap(int[] height)
        {
            int left = 0, right = height.Length - 1;
            
            if (right <= 1)
            {
                return 0;
            }
            
            int leftWall = 0, rightWall = 0;
            int fill = 0;

            while (left < right)
            {
                if (height[left] <= height[right])
                {
                    if (leftWall > height[left])
                    {
                        fill += leftWall - height[left];
                    }
                    else
                    {
                        leftWall = height[left];
                    }
                    left++;
                }
                else
                {
                    if (rightWall > height[right])
                    {
                        fill += rightWall - height[right];
                    }
                    else
                    {
                        rightWall = height[right];
                    }
                    right--;
                }
            }
            return fill;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            int[] height1 = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
            int[] height2 = { 4, 2, 0, 3, 2, 5 };

            Solution test = new Solution();

            Console.WriteLine("Example 1: " + test.Trap(height1));
            Console.WriteLine("Example 2: " + test.Trap(height2));
        }
    }
}
