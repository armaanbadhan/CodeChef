#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t, a, b, c, j;
    cin >> t;
    for(int it = 1; it <= t; it++) {
        cin >> a >> b >> c;
        j = a + b + c;
        if (j == 180) {
            cout << "YES\n";
        }
        else{
            cout << "NO\n";
        }
    }
    return 0;
}