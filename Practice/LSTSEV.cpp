#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    n = n%100;
    n = n/10;
    if (n==7){cout << 1;}
    else {cout << 0;}
    return 0;
}