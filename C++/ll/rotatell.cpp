//https://leetcode.com/problems/rotate-list/
// Input: 1->2->3->4->5->NULL, k = 2
// Output: 4->5->1->2->3->NULL
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
    ListNode* start = head;
    ListNode* mid = head;
    int l=0;
    while(mid->next!=NULL){
        mid = mid->next;
        l++;
    }
    l++;
    k=k%l;
    k=l-k;
    int i=k;
    while(--i>0)
        start=start->next;
    if(k>0){
        mid->next = head;
        head = start->next;
        start->next = NULL;
    }
    return head;            
    }
};