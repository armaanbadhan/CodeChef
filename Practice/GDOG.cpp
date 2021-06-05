#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n, k, a;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n >> k;
        int cnt = 1, max = 0;
        while (cnt<=k){
            a = n%cnt;
            cnt++;
            if (max<a){max=a;}
        }
        cout << max << "\n";
    }
    return 0;
}