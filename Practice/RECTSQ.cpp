#include <bits/stdc++.h>
using namespace std;
#define i_am_speed() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int main(){
    i_am_speed();

    int t, n, m;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n >> m;
        int a = __gcd(n, m);
        int b = n/a * m/a;
        
        cout << b << "\n";
    }
    return 0;
}