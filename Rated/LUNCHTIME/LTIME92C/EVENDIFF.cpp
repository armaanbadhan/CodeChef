#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n;
        int a, o = 0, e = 0;
        for(int in = 0; in < n; in++) {
        cin >> a;
        if (a&1){o+= 1;}
        else{e += 1;}
        }
        if (e > o){cout << o << "\n";}
        else {cout << e << "\n";}
    }
    return 0;
}