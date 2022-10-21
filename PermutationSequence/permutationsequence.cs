using System;
using System.Collections.Generic;

namespace RomanToInt
{
    public class Solution
    {
        public string GetPermutation(int n, int k)
        {
            var list = new List<int>();
            int factorial = 1;
            string rstr = "";

            for (int i = 1; i < n; i++)
            {
                factorial *= i;
                list.Add(i);
            }

            list.Add(n);
            k -= 1;  // Change nth value to index

            while (true)
            {
                rstr += list[(k / factorial)];
                list.RemoveAt(k / factorial);
                
                if (list.Count == 0)
                {
                    break;
                }

                k = k % factorial;
                factorial = factorial / list.Count;
            }
            return rstr;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            int length1 = 3;
            int position1 = 3;
            int length2 = 4;
            int position2 = 9;
            int length3 = 3;
            int position3 = 1;

            Solution test = new Solution();

            Console.WriteLine("Example 1: " + test.GetPermutation(length1, position1));
            Console.WriteLine("Example 2: " + test.GetPermutation(length2, position2));
            Console.WriteLine("Example 3: " + test.GetPermutation(length3, position3));
        }
    }
}
