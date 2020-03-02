int detectloop(Node *head) {
    
    Node* fast = head;
    Node* slow = head;
    while(fast->next!=NULL or slow->next!=NULL){
        fast = fast->next->next;
        slow = slow->next;
        if(fast == slow)
            return 1;
    }
    return 0;
}
