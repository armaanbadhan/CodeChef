#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, d, n;
    cin >> t;
    while (t--) {
        cin >> d >> n;
        while (d--){
            n = (1ll*n*(n+1))/2;
        }
        cout << n << "\n";
    }
    return 0;
}