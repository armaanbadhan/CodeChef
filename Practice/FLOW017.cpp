#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, b, c;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b >> c;
        int ar[3] = {a, b, c};
        sort(ar, ar + 3);
        cout << ar[1] << "\n";
    }
    return 0;
}