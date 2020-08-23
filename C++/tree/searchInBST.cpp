//https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root==NULL)
            return NULL;
        if(root->val==val)
            return root;
        TreeNode* tmp = searchBST(root->left,val);
        if( tmp !=NULL)
            return tmp;
        tmp = searchBST(root->right,val);
        if( tmp !=NULL)
            return tmp;
        return NULL;
    }
};