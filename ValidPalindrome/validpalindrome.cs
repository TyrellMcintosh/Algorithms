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

			List<char> c = new List<char>();

			int i;

			s = s.ToLower(); // convert to lowercase for equality check later

			for (i = 0; i < s.Length; i++)
			{
				if (Char.IsLetter(s[i]) == true || char.IsDigit(s[i]) == true)
					c.Add(s[i]); // add character to list
			}

			int mid = 0;

			len = c.Count;

			if (len == 0 || len == 1)
				return true;

			if (len % 2 == 0) // even
				mid = (len / 2);

			else // odd   
				mid = (int)(len / 2) - 1;
			
			i = 0;
			
			if (mid == 0)
            {
				if (c[i] != c[len - 1 - i])
					return false;
				else
					return true;
			}

			while (i != mid)
			{
				if (c[i] != c[len - 1 - i])
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
			string s3 = "abb";

			Solution test = new Solution();

			Console.WriteLine("Example 1: {0}", test.IsPalindrome(s1));
			Console.WriteLine("Example 2: {0}", test.IsPalindrome(s2));
			Console.WriteLine("Example 3: {0}", test.IsPalindrome(s3));

			Console.ReadLine();
		}
	}
}
