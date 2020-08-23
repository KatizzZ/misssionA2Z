//https://leetcode.com/problems/validate-binary-search-tree/
class Solution {
public:
    bool check(TreeNode* root,long long int min,long long int max){
        if(root==NULL)
            return true;
        if(root->val > min and root->val < max and
           check(root->left,min,root->val) and
           check(root->right,root->val,max))
             return true;
        else return false;
    }
    bool isValidBST(TreeNode* root) {
        return check(root,LONG_MIN,LONG_MAX);
    }
};