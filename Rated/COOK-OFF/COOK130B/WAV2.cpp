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
    int n, q;
    cin >> n >> q;
    int arr[n];
    for (int in = 0; in < n; in++)
    {
        cin >> arr[in];
    }
    int inp;
    for (int iq = 0; iq < q; iq++)
    {
        cin >> inp;
        int neg = 0;
        bool zero = false;
        for (int in = 0; in < n; in++)
        {
            if (arr[in] == inp)zero = true;
            if (arr[in] < inp) neg++;
        }
        if (zero) cout << "0\n";
        else if (neg&1) cout << "NEGATIVE\n";
        else cout << "POSITIVE\n";
    }
}


int main()
{
    file_i_o();
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


void file_i_o()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
}