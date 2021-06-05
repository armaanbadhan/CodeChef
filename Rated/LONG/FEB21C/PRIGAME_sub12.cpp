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


int noofprime(int n){
    int ans = 0;
    while(n>1){
        if(isprime(n)){
            ans+=1;
        }
        n-=1;
    }
    return ans;
}



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, x, y;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> x >> y;
        if(y==1){
            if(x==1 || x==2){cout << "Chef\n";}
            else{cout << "Divyam\n";}}
        else{
            if(noofprime(x) <= y){cout << "Chef\n";}
            else{cout<<"Divyam\n";}
        }
    }
    return 0;
}