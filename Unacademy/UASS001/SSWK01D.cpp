#include <bits/stdc++.h>
using namespace std;
#define i_am_speed() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int main(){
    i_am_speed();

    int t, n;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n;
        int res = 0, temp;
        for (int in = 0; in < n; in++){
            cin >> temp;
            res = res^temp;
        }
        cout << res << "\n";
    }
    return 0;
}