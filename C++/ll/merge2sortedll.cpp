Node* sortedMerge(Node* head1,   Node* head2)
{
    Node* head = (head1->data > head2->data? head2: head1);
    Node* ptr = (head1->data > head2->data? head1: head2);
    //head = head->next;
    while(head->next!=NULL){
        if(head->next==NULL){
            head->next = ptr;
            break;
        }
        if(head->next->data < ptr->data){
            head = head->next;
        }
        else{
            Node* tmp = head->next;
            head->next = ptr;
            ptr = tmp;
        }
    }
}

//https://leetcode.com/problems/merge-two-sorted-lists/
//Recursive appr
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL) return l2;
        if(l2==NULL) return l1;
        if(l1->val < l2->val){
            l1->next = mergeTwoLists(l1->next,l2);
            return l1;
        }
        else{
            l2->next = mergeTwoLists(l1,l2->next);
            return l2;
        }
    }
};