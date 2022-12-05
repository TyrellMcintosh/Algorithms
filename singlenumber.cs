using System;
using System.Collections.Generic;

namespace Test
{
	public class Solution
	{
		public int SingleNumber(int[] nums)
		{
			if (len == 1)
				return nums[0];
            
            

            Array.Sort(nums);
			int len = nums.Length;

			for (int i = 1; i < len - 1; i++)
			{
				if (nums[i-1] != nums[i] && nums[i+1] != nums[i])
					return nums[i];
			}

			if(nums[0] != nums[1])
                return nums[0]; // first number check

			if(nums[len-1] != nums[len-2])
				return nums[len-1]; // last number check
            
            return -1;
		}
	}

	class Program
	{
		static void Main(string[] args)
		{
			int[] nums1 = {2, 2, 1};
			int[] nums2 = {4, 1, 2, 1, 2}; // 1122344
			int[] nums3 = {1};

			Solution test = new Solution();

			Console.WriteLine("Example 1: ", test.SingleNumber(nums1));
			Console.WriteLine("Example 2: ", test.SingleNumber(nums2));
			Console.WriteLine("Example 3: ", test.SingleNumber(nums3));

			Console.ReadLine();
		}
	}
}
