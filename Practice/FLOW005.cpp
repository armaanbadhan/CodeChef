#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    int notes[6] = {100, 50, 10, 5, 2, 1};
    cin >> t;
    for(int it = 1; it <= t; it++) {
        cin >> n;
        int ans = 0;
        for(int i = 0; i < 6; i++) {
            if ( n >= notes[i] ) {
                ans += n / notes[i];
                n = n - (notes[i] * (n / notes[i]));
            }
        }
        cout << ans << "\n";
    }
    return 0;
}