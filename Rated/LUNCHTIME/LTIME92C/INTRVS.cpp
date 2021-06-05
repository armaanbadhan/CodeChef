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
        int a, time = 0, cant = 0;
        bool ti = false, bot = true;
        for(int in = 0; in < n;) {
            cin >> a;
            if (a != -1){time += a;}
            else             {cant += 1;}
            if (a > k){ti = true;}
            if (a > 1 or a == -1){bot = false;}
            in++;
        }
        if (n - cant < (n+1)/2){cout << "Rejected\n";}
        else if (ti){cout << "Too Slow\n";}
        else if (bot){cout << "Bot\n";}
        else {cout << "Accepted\n";}
    }
    return 0;
}