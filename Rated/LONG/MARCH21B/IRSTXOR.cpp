#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, c;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> c;
        int d = 1;
        while (c >= d){
            d *= 2;
        }
        d /= 2;
        d -= 1;
        cout << 1ll*d*(c^d) << "\n";
    }
    return 0;
}
// AC, no idea why this works
// O(t*n) gave TLE
/*

XOR property
13^7=10
7^10=13
10^13=7

*/
