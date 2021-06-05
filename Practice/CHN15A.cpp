#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n, k;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n >> k;
        int temp, ans = 0;
        for(int in = 0; in<n; in++){
            cin >> temp;
            if((temp+k)%7){
                --ans;
            }
        }
        cout << n + ans << "\n";
    }
    return 0;
}