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
        double ans = 0;
        if (n < 1500){
            ans += n*2;
        }
        else{
            ans += 500 + n*1.98;
        }
        cout << fixed << setprecision(2) << ans << "\n";
    }
    return 0;
}