#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);


void solve(){
    int n, k;
    string ss;
    cin >> n >> k >> ss;
    string s = ss + "s";
    int x = 0, max = 0;
    for (int in = 0; in <= n; in++){
        if (s[in] == '*'){
            x += 1;
        }else{
            if(x > max){
                max = x;
            }
            x = 0;
        }
    }
    if (max >= k){
        cout << "yes";
    }else{
        cout << "no";
    }


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
