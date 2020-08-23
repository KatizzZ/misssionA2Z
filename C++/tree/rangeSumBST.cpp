//https://leetcode.com/problems/range-sum-of-bst/
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        int sum=0;
        return s(root,L,R,sum);
    }
    int s(TreeNode* root, int L, int R,int sum){
        if(root==NULL)
            return sum;
        if(root->val >= L and root->val <= R)
            sum+=root->val;
        sum = s(root->left,L,R,sum);
        sum = s(root->right,L,R,sum);
        return sum;
    }
};
/*
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
*/