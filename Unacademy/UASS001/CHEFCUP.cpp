#include <bits/stdc++.h>
using namespace std;
#define i_am_speed() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);


unsigned long long area(int a, int b, int x){
    unsigned long long lol = 1ll*x*(a-x)*(b-x);
    return lol;
}


int main(){
    i_am_speed();

    int t, a, b;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b;
        int lo = 0, hi = min(a, b);
        while (lo <= hi){
            int m1 = lo + (hi - lo)/3, m2 = hi - (hi - lo)/3;
            if (area(a, b ,m1) >= area(a, b, m2)){
                hi = m2-1;
            }
            else{
                lo = m1+1;
            }
        }
        cout << lo << " " << area(a, b, lo) << "\n";
    }
    return 0;
}
