using System;
using System.Collections.Generic;

namespace Test
{
	public class Solution
	{
		public bool IsPalindrome(string s)
		{
			int len = s.Length;

			if (len == 1)
				return true;

			char[] c = new char[len];

			int i;

			for(i = 0; i < s.Length; i++)
			{
				if (Char.IsLetter(s[i]) == true)
					c[i] = s[i]; // copy character to array
				else
					len--; // decrement string length since space is removed
				
			}

			int mid = -1;

			if (len % 2 == 0) // even
				mid = ((len / 2) - 1);

			else // odd   
				mid = (int)(len / 2) - 1;

			i = 0;

			while(i != mid)
			{
				if(c[i] != c[len-1-i])
					return false;
				i++;
			}

			return true;

		}
	}

	class Program
	{
		static void Main(string[] args)
		{
			string s1 = "A man, a plan, a canal: Panama";
			string s2 = "race a car";
			string s3 = " ";

			Solution test = new Solution();

			Console.WriteLine("Example 1: ", test.IsPalindrome(s1));
			Console.WriteLine("Example 2: ", test.IsPalindrome(s2));
			Console.WriteLine("Example 3: ", test.IsPalindrome(s3));
			
			Console.ReadLine();
		}
	}
}
