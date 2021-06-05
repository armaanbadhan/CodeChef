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
        int x = 0, temp;
        for(int in=0; in<n;in++){
            temp = x;
            cin >> x;
            x = temp^x;
        }
        cout << x << "\n";
    }
    return 0;
}