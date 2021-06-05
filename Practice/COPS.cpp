#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, m, x, y;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> m >> x >> y;
        int ar[m], range = x*y, ans = 0;
        for(int im = 0; im < m; im++){
            cin >> ar[im];
        }
        sort(ar, ar + m);

        int flag = ar[0];

        for(int im = 1; im<m;im++){
            int back = 0;
        }

    }
    return 0;
}