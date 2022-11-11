using System;
using System.Collections.Generic;

namespace Power
{
    public class Solution
    {
        public double MyPow(double x, int n)
        {
            if (x == 0 || x == 1 || x == -1)  // 0ⁿ = 0, 1ⁿ = 1, -1ⁿ = -1
                return x;

            if (n == 0)	// x⁰ = 1
            	return (double)1;

            if (n == -1) // x⁻¹ = 1 / x
            	return (1 / x);

            double rdouble = x;
            bool flag = false;	// Check if power is negative

            if (n < 0)
            {
                flag = true;
                n *= -1;    // convert to positive
            }

            int count = 1;

            while (count != n)  // 5^3
            {
                rdouble *= x;
                count++;
            }

            if (flag == true)	// power is negative
                return (1 / rdouble);

            return rdouble;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            double x1 = 2.00000;
            double x2 = 2.10000;
            double x3 = 2.00000;

            int n1 = 10;
            int n2 = 3;
            int n3 = -2;

            Solution test = new Solution();

            Console.WriteLine("Example 1: {0}", test.MyPow(x1, n1));
            Console.WriteLine("Example 2: {0}", test.MyPow(x2, n2));
            Console.WriteLine("Example 3: {0}", test.MyPow(x3, n3));

            Console.ReadLine();
        }
    }
}
