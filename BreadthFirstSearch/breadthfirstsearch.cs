using System;
using System.Collections.Generic;

namespace BST
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;

        public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public class BinarySearchTree
    {
        public TreeNode insert(TreeNode root, int v)
        {
            if (root == null)
            {
                root = new TreeNode();
                root.val = v;
            }

            else if (v < root.val)
            {
                root.left = insert(root.left, v);
            }
            else
            {
                root.right = insert(root.right, v);
            }

            return root;
        }

        public IList<IList<int>> LevelOrder(TreeNode root)
        {
            IList<IList<int>> rlist = new List<IList<int>>();

            if (root == null)
                return rlist;

            Queue<TreeNode> queue = new Queue<TreeNode>();
            
            int depth = 0;
            int count = 1;

            queue.Enqueue(root);

            rlist.Insert(depth,new List<int>());

            while (queue.Count != 0)
            {
                TreeNode head = queue.Dequeue();
                count--;
                rlist[depth].Add(head.val);

                if (head.left != null)
                    queue.Enqueue(head.left);

                if (head.right != null)
                    queue.Enqueue(head.right);

                if (count == 0 && queue.Count > 0)
                {
                    count = queue.Count;
                    depth++;
                    rlist.Insert(depth,new List<int>());
                }
            }

            return rlist;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            TreeNode root = null;

            BinarySearchTree bst = new BinarySearchTree();

            IList<IList<int>> nodes = new List<List<int>>();

            int[] arr1 = { 3, 9, 20, 15, 7 };

            foreach (int x in arr1)
            {
                root = bst.insert(root, x);
            }

            nodes = bst.LevelOrder(root);

            Console.ReadLine();
        }
    }
}
