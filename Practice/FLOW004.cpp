#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n, k, l;
    cin >> t;
    for(int it = 1; it <= t; it++) {
        cin >> n;
        k = n % 10;
        l = n;
        while (l >= 10){
            l = l / 10;
        }
        cout << k + l << "\n";
    }
    return 0;
}