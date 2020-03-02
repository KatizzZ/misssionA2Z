//#include<bits/stdc++.h>
#include<iostream>
#include<sstream>
#include<map>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        getchar();
        map<string,int> mp;
        string str,word;
        getline(cin,str);
        stringstream ss(str);
        while(ss>>word)
            mp[word]++;
        map<string, int>::iterator m;
        int len=0,flag=1;
        string fw;
        for(m=mp.begin(); m!=mp.end(); m++){
            if(len <= m->second)
            {
                flag = 1;
                fw = m->first;
                len = m->second;
            //cout<< m->first <<"->";
            //cout<< m->second <<endl;
            }
            if(len == m->second && flag){
                flag = 0;
                fw = m->first;
                len = m->second;
                cout<< m->first <<"->";
                cout<< m->second <<endl;
            }
            //cout<< m->first <<"->";
            //cout<< m->second <<endl;
        }
        cout<<fw<<endl;
    }
	return 0;
}