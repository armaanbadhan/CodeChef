#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    cin >> t;
    for(int it = 1; it <= t; it++) {
        cin >> n;
        int ans = 0;
        ans = sqrt(n);
        cout << ans << "\n";
    }
    return 0;
}