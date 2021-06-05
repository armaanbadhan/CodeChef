#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    cin >> t;
    while (t--) {
        long long ans = 1;
        cin >> n;
        while (n--){
            ans = ans * (n + 1);
        }
        cout << ans << "\n";
    }
    return 0;
}