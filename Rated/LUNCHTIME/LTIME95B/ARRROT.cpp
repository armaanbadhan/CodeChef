#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);
void file_i_o();


void solve()
{
    ull n, q, sum = 0, temp;
    cin >> n;
    for (int in = 0; in < n; in++)
    {
        cin >> temp;
        sum += temp;
        sum %= MOD;
    }
    cin >> q;
    for (int iq = 0; iq < q; iq++)
    {
        cin >> temp;
        sum *= 2;
        sum %= MOD;
        cout << sum << "\n";
    }
    cout << "\n";
}


int main()
{
    file_i_o();
    i_am_speed();

    int t = 1;
    //cin >> t;
    for(int it = 0; it < t; it++)
    {
        #ifndef ONLINE_JUDGE
            cout << "\tTest Case " << it+1 << ":\n";
        #endif
        solve();
    }
    return 0;
}


void file_i_o()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
}