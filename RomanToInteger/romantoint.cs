using System;
using System.Collections;

namespace RomanToInt
{
	public class Solution 
	{
		public int RomanToInt(string s)
		{
			int ans = 0;

			if (s.Length < 1 || s.Length > 15)	// Constraint: 1 <= s.Length <= 15
			{
				Console.WriteLine("The given string is either too short or too long");
				return 0;
			}

			Hashtable roman = new Hashtable()
			{
				{'I', 1},
				{'V', 5},
				{'X', 10},
				{'L', 50},
				{'C', 100},
				{'D', 500},
				{'M', 1000}
			};
			
			ans += (int)roman[s[0]];
			
			for (int i = 1; i < s.Length; i++)
			{
				if ((int)roman[s[i]] > (int)roman[s[i-1]])
				{
					ans += (int)roman[s[i]] - (int)roman[s[i-1]] - (int)roman[s[i-1]];
				}
				else
				{
					ans += (int)roman[s[i]];
				}
			}
			return ans;
		}
    }

	class Program
	{
		static void Main(string[] args)
		{
			string rom1 = "III";
			string rom2 = "LVIII";
			string rom3 = "MCMXCIV";
			
			Solution test = new Solution();

			Console.WriteLine("Example 1: " + test.RomanToInt(rom1));
			Console.WriteLine("\nExample 2: " + test.RomanToInt(rom2));
			Console.WriteLine("\nExample 3: " + test.RomanToInt(rom3));
		}
	}
}
