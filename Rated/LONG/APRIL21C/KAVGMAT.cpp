#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);


void solve(){
    int n, m;
    double K;
    ull res = 0;
    cin >> n >> m >> K;
    ll arr[n+1][m+1];

    for (int im = 0; im <= m; im++){
        arr[0][im] = 0;
    }

    for (int in = 1; in <= n; in++){
        arr[in][0] = 0;
        for (int im = 1; im <= m; im++){
            cin >> arr[in][im];
        }
    }

    for (int in = 0; in <= n; in++){
        for (int im = 1; im <= m; im++){
            arr[in][im] += arr[in][im-1];
        }
    }

    for (int im = 0; im <= m; im++){
        for (int in = 1; in <= n; in++){
            arr[in][im] += arr[in-1][im];
        }
    }

/*
    for (int in = 0; in <= n; in++){
        for (int im = 0; im <= m; im++){
            cout << arr[in][im] << " ";
        }
        cout << endl;
    }
*/
    for (int in = 0; in < n; in++){
        for (int im = 0; im < m; im++){
            int x = min(n - in, m - im);
            ull temp = 0;
            for (int k = 0; k < x; k++){
                ull pref = arr[in+k+1][im+k+1] - arr[in][im+k+1] - arr[in+k+1][im] + arr[in][im];
                ll cnt = (k+1)*(k+1);
                double val = pref/cnt;
                //cout << pref << " " << in << " " << im << " " << k << endl;
                if (val >= K){
                    temp = x - k;
                    break;
                }
            }
            res += temp;
        }
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
