//https://practice.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1
int diff(Node *root, int k, int min){
    if(root==NULL)
        return min;
    //cout<<root->data<<","<<k<<" ";
    if(abs(root->data-k)<abs(min)){
        min=abs(root->data-k);
    }
    min = diff(root->left,k,min);
    min = diff(root->right,k,min);
    return min;    
}
int maxDiff(Node *root, int k)
{
    return diff(root,k,abs(root->data-k));
}