//https://leetcode.com/problems/binary-tree-inorder-traversal/
//recursion
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> v;
        inorder(root,v);
        return v;
    }
    void inorder(TreeNode* root, vector<int> &v){
        if(root==NULL)
            return;
        inorder(root->left,v);
        v.push_back(root->val);
        inorder(root->right,v);
    }
};
//using stack no recursion
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> v;
        stack<TreeNode*> s;
        TreeNode* current = root;
        while(current!= NULL || s.empty() == false){
            while(current!=NULL){
                s.push(current);
                current = current->left;
            }
            current = s.top();
            s.pop();
            v.push_back(current->val);
            current=current->right;
        }
        return v;
    }
};