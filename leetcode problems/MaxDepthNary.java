559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:
         1
      /  |  \
     3   2   4
    /\
   5  6

We should return its max depth, which is 3.

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

import java.util.Queue;
class Solution {
    public int maxDepth(Node root) {
        if (root==null){
            return 0;
        }
        Queue<Node> q= new LinkedList<Node>();
        q.add(root);
        int counter=0;

        while(!q.isEmpty()){
            int queueSize=q.size();
            for(int i=0;i<queueSize;i++){
                Node current = q.poll();
                for(Node n:current.children){
                    q.add(n);
                }
            }
            counter+=1;
        }
        return counter;
    }
}
