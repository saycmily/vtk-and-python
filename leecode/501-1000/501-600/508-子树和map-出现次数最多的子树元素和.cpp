/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> jihe;
    vector<int> findFrequentTreeSum(TreeNode* root) {
        if (root == NULL)
            return {};
        jihe.emplace_back(complete(root));
        map<int, int> cm;
        for (int sum : jihe) {
            if (cm.count(sum) == 1)
                cm[sum] ++;
            else 
                cm[sum] = 1;
        }
        vector<int> ans;
        int cur;
        for (map<int, int>::iterator c = cm.begin(); c != cm.end(); c++) {
            if (ans.size() == 0) {
                ans.emplace_back(c -> first);
                cur = c -> second;
                continue;
            } 
            if ((c -> second) > cur) {
                ans.clear();
                ans.emplace_back(c -> first);
                cur = c -> second;
            } else if ((c -> second) == cur) {
                ans.emplace_back(c -> first);
            }
        }
        return ans;
    }
    int complete(TreeNode* root) {
        int l = 0, r = 0;
        if (root -> left) {
            l = complete(root -> left);
            jihe.emplace_back(l);
        }
        if (root -> right) {
            r = complete(root -> right);
            jihe.emplace_back(r);
        }
        return l + r + root->val;
    }
};