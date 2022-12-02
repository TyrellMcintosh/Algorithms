using System;
using System.Collections.Generic;

namespace GasStation
{
    public class Solution
    {
        public int CanCompleteCircuit(int[] gas, int[] cost)
        {
            int fuel = 0;
            int len = gas.Length;

            for (int i = 0; i < len; i++)
                fuel += gas[i] - cost[i];

            if (fuel < 0)
            	return -1;	// cost exceeds gas so cannot make the trip

            fuel = 0;
            int ind = 0;

            for (int i = 0; i < len; i++)
            {
            	if (fuel < 0)
            	{
            		ind = i;	// index to return
            		fuel = 0;	// reset fuel
            	}

            	fuel += gas[i] - cost[i];
            }

            return ind;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            int[] gas1 = { 1, 2, 3, 4, 5 };
            int[] cost1 = { 3, 4, 5, 1, 2 };

            int[] gas2 = { 2, 3, 4 };
            int[] cost2 = { 3, 4, 3 };

            int[] gas3 = {5, 8, 2, 8};
            int[] cost3 = {6, 5, 6, 6};

            int[] gas4 = {1, 1, 3};
            int[] cost4 = {2, 2, 1};

            Solution test = new Solution();

            Console.WriteLine("Example 1: {0}", test.CanCompleteCircuit(gas1, cost1));
            Console.WriteLine("Example 2: {0}", test.CanCompleteCircuit(gas2, cost2));
            Console.WriteLine("Example 3: {0}", test.CanCompleteCircuit(gas3, cost3));
            Console.WriteLine("Example 4: {0}", test.CanCompleteCircuit(gas4, cost4));

            Console.ReadLine();
        }
    }
}
