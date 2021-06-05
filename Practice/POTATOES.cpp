#include <bits/stdc++.h>
using namespace std;

bool isprime(int x){
    if(x<2)return false;
    if(x<4)return true;
    if((x&1)==0)return false;
    if(x%3==0)return false;
    int curr=5, s=sqrt(x);
    while(curr<=s){
        if((x%curr)==0)return false;
        curr+=2;
        if((x%curr)==0)return false;
        curr += 4;
    }
    return true;
}


int nextprime(int x){
    if(isprime(x)){
        return x;
    }
    return nextprime(x+1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, b;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b;
        a = a+b+1;
        cout << nextprime(a)-a+1 << "\n";
    }
    return 0;
}