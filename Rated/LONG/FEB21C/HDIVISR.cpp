#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, i = 10;
    cin >> n;
    while(n%i){i--;}
    cout << i;
    return 0;
}
// duh