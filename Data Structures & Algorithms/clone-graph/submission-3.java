/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        Map<Node, Node> hashNode = new HashMap();

        return cloneDFS(node, hashNode);
    }

    private Node cloneDFS(Node node, Map<Node, Node> hashNode){
        if (node == null) return null;
        if (hashNode.containsKey(node)) 
            return hashNode.get(node);

        Node clone = new Node(node.val);
        hashNode.put(node, clone);
        for (Node neighbor : node.neighbors){
            clone.neighbors.add(cloneDFS(neighbor, hashNode));
        }
        
        return clone;
    }
}