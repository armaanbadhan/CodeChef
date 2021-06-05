#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);


void solve()
{
    int n;
    cin >> n;
    double vv, dec[n];
    cin >> vv;
    vv = vv*100;
    int v = vv;
    int res = 0;
    for (int in = 0; in < n; in++)
    {
        cin >> dec[in];
    }
    int arr[n];
    for (int in = 0; in < n; in++)
    {
        double x = dec[in]*100;
        arr[in] = x;
    }
    for (int in = 0; in < n; in++)
    {
        int temp = v/arr[n-in-1];
        v -= temp*arr[n-in-1];
        res += temp;
        if (v == 0)
        {
            break;
        }
    }
    if (v == 0)
    {
        cout << res;
    }
    else
    {
        cout << 0;
    }
    cout << "\n";
}


int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    i_am_speed();

    int t = 1;
    // cin >> t;
    for(int it = 0; it < t; it++)
    {
        #ifndef ONLINE_JUDGE
            cout << "\tTest Case " << it+1 << ":\n";
        #endif
        solve();
    }
    return 0;
}
