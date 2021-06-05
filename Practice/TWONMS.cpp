#include <bits/stdc++.h>
using namespace std;
#define i_am_speed() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int main(){
    i_am_speed();

    int t, n, a, b;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b >> n;
        if (n&1) {
            a *= 2;
        }
        if (a>b){
            cout << a/b << "\n";
        }
        else{
            cout << b/a << "\n";
        }
    }
    return 0;
}