#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, b;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b;
        double ans = a*b;
        if (a >= 1000){
            ans = ans*9/10;
        }
        cout << fixed << setprecision(6) << ans << "\n";
    }
    return 0;
}