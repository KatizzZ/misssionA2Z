//https://leetcode.com/problems/invert-binary-tree/submissions/
//Using queue //RT- 0ms, memory=10.2 
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL)
            return NULL;
        TreeNode *head = root;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode *curr = q.front(),*tmp;
            q.pop();
            if(curr!=NULL){
                tmp = curr->left;
                curr->left = curr->right;
                curr->right = tmp;
                if(curr->left or curr->right){
                    q.push(curr->left);
                    q.push(curr->right);
                }
            }
        }
        return head;
    }
};

//using recursion RT- 4ms, memory=10.1 
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL)
            return NULL;
        TreeNode *tmp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(tmp);
        return root;
    }
};