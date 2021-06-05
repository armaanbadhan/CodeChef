#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    cin >> t;
    for(int it = 0; it < t; it++){
        cin >> n;
        int ar[n];
        cin >> ar[0] >> ar[1];
        int g = __gcd(ar[0], ar[1]);
        for(int in = 2; in<n; in++){
            cin >> ar[in];
            g = __gcd(g, ar[in]);        
        }
        for(int in=0;in<n;in++){
            cout << ar[in]/g << " ";
        }
        cout << "\n";
    }
    return 0;
}