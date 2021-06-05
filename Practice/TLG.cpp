#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, b, x = 0, y = 0, lead = 0, w, temp;
    cin >> t;
    while (t--) {
        cin >> a >> b;
        x += a; y += b;
        if (x > y) {
            temp = x - y;
            if (temp > lead){
                lead = temp;
                w = 1;
            }
        }
        else{
            temp = y - x;
            if (temp > lead){
                lead = temp;
                w = 2;
            }
        }
    }
    cout << w << " " << lead;
    return 0;
}