#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    int menu[12] = {2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1};
    cin >> t;
    for(int it = 0; it < t;) {
        cin >> n;
        int ans = 0;
        for(int i = 0; i < 12;) {
            if ( n >= menu[i] ) {
                ans += n / menu[i];
                n = n - (menu[i] * (n / menu[i]));
            }
            i++;
        }
        cout << ans << "\n";
        it++;
    }
    return 0;
}