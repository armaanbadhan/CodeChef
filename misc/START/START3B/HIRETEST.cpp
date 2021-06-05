#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);
void file_i_o();

char ch;

void solve()
{
    int n, m;
    cin >> n >> m;
    int x, y;
    cin >> x >> y;
    string res = "";
    for (int in = 0; in < n; in++)
    {
        int pcnt = 0, fcnt = 0;
        for (int im = 0; im < m; im++)
        {
            cin >> ch;
            if (ch == 'P')pcnt++;
            if (ch == 'F')fcnt++;
        }
        if (fcnt >= x) res += "1";
        else if (fcnt+1 >= x && pcnt >= y) res += "1";
        else res += "0";
    }
    cout << res;
    cout << "\n";
}


int main()
{
    file_i_o();
    i_am_speed();

    int t = 1;
    cin >> t;
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