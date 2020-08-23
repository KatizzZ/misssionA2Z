//https://leetcode.com/problems/reverse-linked-list/submissions/
//Recurssion
ListNode* reverse(ListNode* head){
        if(head==NULL) return head;
        if(head->next == NULL) return head;
        ListNode* tmp = reverse(head->next);
        head->next->next=head;
        head->next=NULL;
        return tmp;
}
//iterative
Node* reverseList(Node *head)
{
    if(head==NULL)
        return head;
    Node* curr = head;
    Node* prev = NULL;
    Node* next = NULL;
    while(curr!=NULL){
        next=curr->next;
        curr->next=prev;
        prev=curr;
        curr=next;
    }
    head=prev;
    return head;
}
//print
void reverseprint(Node* head){
    if(head==NULL)
        return;
    reverseprint(head->next);
    cout<<head->data<<" ";
}