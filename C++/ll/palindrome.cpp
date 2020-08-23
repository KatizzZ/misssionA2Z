bool isPalindrome(Node *head)
{
    if(head==NULL)
        return 0;
    Node* fast = head;
    Node* slow = head;
    Node* len = head;
    int n=0;
    stack<int> s;
    s.push(slow->data);
    while(len!=NULL){
        len = len->next;
        n++;
        if(fast!=NULL and fast->next!=NULL){
            fast=fast->next->next;
            if(fast!=NULL)
            {
                slow=slow->next;
                s.push(slow->data);
            }
        }
    }
    if(n%2!=0)
        s.pop();
    slow=slow->next;
    while(slow!=NULL){
        if(slow->data!=s.top()){
            return 0;
        }
        slow=slow->next;
        s.pop();
    }
    return 1;
}