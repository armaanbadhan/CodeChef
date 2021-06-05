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
        int ar[n];
        for(int in = 0; in < n; in++){
            cin >>ar[in];
        }
        sort(ar, ar+n);
        cout << ar[0]+ar[1] << "\n";
    }
    return 0;
}