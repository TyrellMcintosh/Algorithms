using System;
using System.Collections.Generic;

namespace SearchMatrix
{
    public class Solution
    {
        public bool SearchMatrix(int[][] matrix, int target)
        {
            int rsize = matrix.Length - 1;
            int csize = matrix[0].Length;

            if (rsize == 0)
            {
                if (target >= matrix[0][0])
                {
                    for (int i = 0; i < csize; i++)
                    {
                        if (matrix[0][i] == target)
                        {
                            return true;
                        }
                    }
                    return false;
                }
                else
                    return false;
            }

            for (int i = 0; i < rsize; i++)
            {
                if (matrix[i][0] <= target && matrix[i + 1][0] > target)
                {
                    for (int j = 0; j < csize; j++)
                    {
                        if (matrix[i][j] == target)
                        {
                            return true;
                        }
                    }
                    return false;
                }
            }

            if (matrix[rsize][0] <= target) // Last row to be checked
            {
                for (int j = 0; j < csize; j++)
                {
                    if (matrix[rsize][j] == target)
                    {
                        return true;
                    }
                }
            }

            return false;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            int[][] matrix1 = new int[3][];
            matrix1[0] = new int[4] { 1, 3, 5, 7 };
            matrix1[1] = new int[4] {10, 11, 16, 20};
            matrix1[2] = new int[4] { 23, 30, 34, 60 };

            int target1 = 3;
            int target2 = 13;

            Solution test = new Solution();

            Console.WriteLine("Example 1: " + test.SearchMatrix(matrix1, target1));
            Console.WriteLine("Example 2: " + test.SearchMatrix(matrix1, target2));
        }
    }
}
