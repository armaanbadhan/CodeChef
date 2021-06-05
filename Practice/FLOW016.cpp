#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, b, temp;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b;
        int x = a, y = b;
        if (x < y){
            x = x + y;
            y = x - y;
            x = x - y;
        }
        while (x%y){
            temp = x;
            x = y;
            y = temp % y;
        }
        cout << y << " " << 1ll*(a/y)*b << "\n";
    }
    return 0;
}