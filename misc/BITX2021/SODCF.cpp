#include <bits/stdc++.h>
using namespace std;
#define i_am_speed() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ll long long

int main(){
    i_am_speed();

    int t, n;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n;
        ll arr[n] = {}, ssumm = 0, x;
        for (int in = 0; in < n; in++){
            cin >> x;
            arr[in] = x;
            ssumm += x;
        }
        ll res = ssumm;
        for (int ii = 0; ii < n; ii++){
            for (int ij = 0; ij < n; ij++){
                ll temp = 0;
                for (int k = ii; k < ij; k++){
                    temp += arr[k];
                }
                res = max(ssumm + 2*temp, res);
            }
        }
        cout << res << "\n";
    }
    return 0;
}