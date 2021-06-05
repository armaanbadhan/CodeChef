#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    int ar[t];
    for(int it = 0; it < t; it++) {cin >> ar[it];}
    sort(ar, ar + t);
    for(int jt = 0; jt < t; jt++) {cout << ar[jt] << "\n";}
    return 0;
}