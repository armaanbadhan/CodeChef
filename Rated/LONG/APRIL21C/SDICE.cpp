#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);


void solve(){
    ull n;
    cin >> n;
    int left = n%4;
    ull stacked = n/4;
    // top face -> 4; bottom -> 3
    // in(touching) -> 1, 2; out -> 5, 6
    ull res = stacked*44;
    if(left==1){res += 20*1;}
    if(left==2){res += 6+6+7+7+5+5;}
    if(left==3){res += 6+6+6+7+7+5+4+5+5;}
    if(stacked>0){
        res += 4*(4-left);
    }
    cout << res;
    cout << "\n";
}


int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    i_am_speed();

    int t = 1;
    cin >> t;
    for(int it = 0; it < t; it++){
        #ifndef ONLINE_JUDGE
            cout << "\tTest Case " << it+1 << ":\n";
        #endif
        solve();
    }
    return 0;
}
