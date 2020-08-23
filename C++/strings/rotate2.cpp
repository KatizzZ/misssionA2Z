//#include<bits/stdc++.h>
#include<iostream>
#include<string.h>
using namespace std;
int getMiddle(Node *head)
{
   Node *fast = head;
   Node *slow = head;
   while(fast->next!=NULL){
       fast = fast->next->next;
       slow = slow->next;
   }
    return slow->data;
}
int main()
{
    int t;
    cin>>t;
    while(t--){
        string str,strf,strd;
        cin>>str;//>>strf;
        strd = str+str;
        int l = str.length();
        if(l==1){
            cout<<1<<endl;
            continue;
        }
        if(strf==strd.substr(2,l) or strf==strd.substr(l-2,l))
            cout<<1<<endl;
        else
            cout<<0<<endl;
        // cout<<(strd.substr(2,l))<<endl;
        // cout<<(strd.substr(l-2,l))<<endl;
    }
	return 0;
}