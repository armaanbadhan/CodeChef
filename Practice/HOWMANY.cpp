#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);


void solve(){
    int n, ans = 0;
    cin >> n;
    if((n/10) == 0){cout<<1;}    
    else if((n/100) == 0){cout<<2;}
    else if((n/1000) == 0){cout<<3;}
    else{cout<<"More than 3 digits";}
    cout << "\n";
}


int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    i_am_speed();

    int t = 1;
    //cin >> t;
    for(int it = 0; it < t; it++){
        cout << "\tTest Case " << it+1 << ":\n";
        solve();
    }
    return 0;
}
