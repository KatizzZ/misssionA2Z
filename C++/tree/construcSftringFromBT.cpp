//https://leetcode.com/problems/construct-string-from-binary-tree/
class Solution {
public:
    string tree2str(TreeNode* t) {
        string str;
        return tree(t,str);
    }
    string tree(TreeNode* t,string str) {
        if(t==NULL)
            return str;
        str += to_string(t->val);
        if(t->left!=NULL){
            str+="(";
            str = tree(t->left,str);
            str+=")";
        }
        //else return str;
        if(t->right!=NULL){
            if(t->left==NULL)
            str+="()";
            str+="(";
            str = tree(t->right,str);
            str+=")";
        }
        return str;
    }
};
/*
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"
*/