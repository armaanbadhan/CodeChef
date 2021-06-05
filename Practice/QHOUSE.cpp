#include <iostream>
using namespace std;

#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);
#define debug(a) cout << a << endl
#define debug2(a, b) cout << a << " " << b << endl;

typedef long long ll;
typedef unsigned long long ull;

void file_i_o();

/*
ASCII VALUES 'A' -> 65, 'Z' -> 90, 'a' -> 96, 'z' -> 122, '0' -> 48;
INT_MAX -> 2,147,483,647 (10^10), LLONG_MAX -> 9,223,372,036,854,775,807 (10^19)
*///////////////////////////////////////////////////////////////////////////////

/*

*/

void solve()
{
    int lo = 0, hi = 1000, mid, half_len;
    ull res = 0;
    string inp;
    while (lo <= hi)
    {
        mid = (lo+hi)/2;
        cout << "? " << mid << " " << 0 << endl;
        cin >> inp;
        if (inp == "YES")
        {
            half_len = mid;
            lo = mid + 1;
        }
        else
        {
            hi = mid - 1;
        }
    }
    res += half_len*half_len*4*1ll;
    int base;
    lo = half_len;
    hi = 1000;
    while (lo <= hi)
    {
        mid = (hi+lo)/2;
        cout << "? " << mid << " " << 2*half_len << endl; /////
        cin >> inp;
        if (inp == "YES")
        {
            base = mid;
            lo = mid + 1;
        }
        else
        {
            hi = mid - 1;
        }
    }
    int height;
    lo = half_len*2;
    hi = 1000;
    while (lo <= hi)
    {
        mid = (lo + hi)/2;
        cout << "? " << 0 << " " << mid << endl;
        cin >> inp;
        if (inp == "YES")
        {
            height = mid;
            lo = mid + 1;
        }
        else
        {
            hi = mid - 1;
        }
    }
    // cout << height << " " << base << " " << half_len;
    res += ((height - 2*half_len)*base*1ll);
    cout << "! " << res;
    cout << "\n";
}


int main()
{
    //file_i_o();
    //i_am_speed();

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


void file_i_o()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
}