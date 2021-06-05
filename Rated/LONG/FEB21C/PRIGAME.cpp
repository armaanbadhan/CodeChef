#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, x, y;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> x >> y;
        int ans = 0;
        
        cout << ans << "\n";
    }
    return 0;
}


// chef can only win in first move
// chef only wins if (number of primes <= to x) are <= y  
// using loops resulted in O(t*x*√x) => TLE