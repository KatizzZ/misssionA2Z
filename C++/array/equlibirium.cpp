
#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,lsum=0,rsum=0,flag=0;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++){
            cin>>arr[i];
            rsum+=arr[i];
        }
        for(int i=0; i<n; i++){
            if(lsum==rsum-arr[i]){
                cout<<arr[i]<<endl;
                flag=1;
                break;
            }
            lsum+=arr[i];
            rsum-=arr[i];
        }
        if(flag==0)
            cout<<"-1"<<endl;
    }
    return 0;
}