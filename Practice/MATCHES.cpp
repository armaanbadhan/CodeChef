#include <bits/stdc++.h>
using namespace std;
#define i_am_speed() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int main(){
    i_am_speed();

    int t, a, b, arr[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b;
        a += b;
        int ans = 0;
        while(a){
            ans += arr[a%10];
            a /= 10;
        }
        cout << ans << "\n";
    }
    return 0;
}