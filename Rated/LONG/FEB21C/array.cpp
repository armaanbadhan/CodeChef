#include <bits/stdc++.h>
using namespace std;


bool isprime(int x){
    if(x<2)return false;
    if(x<4)return true;
    if((x&1)==0)return false;
    if(x%3==0)return false;
    int i = 5, s = sqrt(x)+1;
    while(i<=s){
        if(x%i==0){
            return false;
        }
        i+=2;
        if(x%i==0){
            return false;
        }
        i+=4;
    }
    return true;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int arr[100001], x = 0;
    for(int i = 0; i<100001; i++){
        if(isprime(i+1)){x+=1;}
        arr[i] = x;
    }
    for(int i = 0;i<100000;i++){
        cout << arr[i] << ",";
    }
}
