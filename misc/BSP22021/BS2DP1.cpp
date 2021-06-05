#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long t, n, ans = 0;
    cin >> t;
    long long ar[t];
    cin >> n;
    for(int it = 0; it < t;) {
        cin >> ar[it];
        if (ar[it] > 0) {
            ans += ar[it];
        }
        it++;
    }
    sort(ar, ar + t);
    for (int ij = 0; ij < n;) {
        if (ar[ij] < 0) {
            ans -= ar[ij];
        }
        ij++;
    }
    cout << ans;
    return 0;
}