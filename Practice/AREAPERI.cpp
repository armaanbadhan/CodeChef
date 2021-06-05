#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int l, b;
    cin >> l >> b;
    int p = 2*l + 2*b, a = l*b;
    if(p>a){cout<<"Peri\n"<<p;}
    else if(a>p){cout<<"Area\n"<<a;}
    else{cout<<"Eq\n"<<a;}

    return 0;
}