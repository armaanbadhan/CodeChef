#include <iostream>
#include<cmath>
using namespace std;

#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);

typedef long long ll;
typedef unsigned long long ull;

void file_i_o();

/*
ASCII VALUES 'A' -> 65, 'Z' -> 90, 'a' -> 96, 'z' -> 122, '0' -> 48;
INT_MAX -> 2,147,483,647 (10^10), LLONG_MAX -> 9,223,372,036,854,775,807 (10^19)
*/


ull modPow(int exp)
{
    if (exp == 0)
    {
        return 1;
    }
    if (exp == 1)
    {
        return 2;
    }
    ull prev = modPow(exp / 2);
    if (exp&1)
    {
        return (2*prev*prev) % MOD;
    }
    else
    {
        return (prev*prev) % MOD;
    }
}



void solve()
{
    int n;
    cin >> n;
    // ull mex = pow(2, n);
    // int res = 0;
    // for (int x = 0; x < mex; x++)
    // {
    //     if (((x)^(x+1)) == ((x+2)^(x+3)))
    //     {
    //         //cout << x << " ";
    //         res++;
    //     }
    // }
    // cout << res;
    ull res = modPow(n-1);
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