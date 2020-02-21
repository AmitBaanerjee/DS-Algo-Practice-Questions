# 589. N-ary Tree Preorder Traversal
#
# Given an n-ary tree, return the preorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:
#
#              1
#           /  |  \
#          3   2   4
#         / \
#        5   6

# Return its preorder traversal as: [1,3,5,6,2,4].

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public List<Integer> preorder(Node root) {
        if (root==null)
            return new ArrayList<Integer>();
        List<Integer> l=new ArrayList<Integer>();
        Stack<Node> s=new Stack<Node>();
        int length;
        s.push(root);
        while(!s.isEmpty()){
            Node curr=s.pop();
            l.add(curr.val);
            length=curr.children.size();
            if (length==0)
                continue;
            else{
                for(int i =length-1;i>=0;i--){
                    s.push(curr.children.get(i));
                }
            }
        }
        return l;
        
    }
}
