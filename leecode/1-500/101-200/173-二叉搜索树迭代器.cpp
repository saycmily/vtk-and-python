/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class BSTIterator {
public:
    vector<int> tree;
    int num = 0;
    BSTIterator(TreeNode* root) {
        if(root == nullptr) return;
        stack<TreeNode*> st;
        while(root || !st.empty()) {
            while(root){
                st.push(root);
                root = root -> left;
            }
            if(!st.empty()) {
                root = st.top(); st.pop();
                tree.emplace_back(root -> val);
                root = root -> right;
            }
        }
    }
    int next() {
        return tree[num++];
    }
    bool hasNext() {
        if (num == tree.size()) return false;
        return true;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */