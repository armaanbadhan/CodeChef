#include <iostream>
using namespace std;

#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);
#define debug(a) cout << a << endl
#define debug2(a, b) cout << a << " " << b << endl

typedef long long ll;
typedef unsigned long long ull;

void file_i_o();

/*
ASCII VALUES 'A' -> 65, 'Z' -> 90, 'a' -> 96, 'z' -> 122, '0' -> 48;
INT_MAX -> 2,147,483,647 (10^10), LLONG_MAX -> 9,223,372,036,854,775,807 (10^19)
*///////////////////////////////////////////////////////////////////////////////

/*

*/

void solve(){
    ll n, m;
    ull K;
    ull res = 0;
    cin >> n >> m >> K;
    ll arr[n+1][m+1];

    for (int im = 0; im <= m; im++)
    {
        arr[0][im] = 0;
    }

    for (int in = 1; in <= n; in++)
    {
        arr[in][0] = 0;
        for (int im = 1; im <= m; im++)
        {
            cin >> arr[in][im];
        }
    }

    // prefix sum
    for (int in = 0; in <= n; in++)
    {
        for (int im = 1; im <= m; im++)
        {
            arr[in][im] += arr[in][im-1];
        }
    }

    // prefix sum
    for (int im = 0; im <= m; im++)
    {
        for (int in = 1; in <= n; in++)
        {
            arr[in][im] += arr[in-1][im];
        }
    }

    // PRINTS THE ARRAY
    // for (int in = 0; in <= n; in++)
    // {
    //     for (int im = 0; im <= m; im++)
    //     {
    //         cout << arr[in][im] << " ";
    //     }
    //     cout << endl;
    // }

    // GAVE TLE, LINEAR SEARCH
    // use K as double!!!!!!!!!!
    // for (int in = 0; in < n; in++)
    // {
    //     for (int im = 0; im < m; im++)
    //     {
    //         int x = min(n - in, m - im);
    //         ull temp = 0;
    //         for (int k = 0; k < x; k++)
    //         {
    //             ull pref = arr[in+k+1][im+k+1] - arr[in][im+k+1] - arr[in+k+1][im] + arr[in][im];
    //             ll cnt = (k+1)*(k+1);
    //             double val = pref/cnt;
    //             //cout << pref << " " << in << " " << im << " " << k << endl;
    //             if (val >= K)
    //             {
    //                 temp = x - k;
    //                 break;
    //             }
    //         }
    //         res += temp;
    //     }
    // }


    // BINARY SEARCH, AC
    // res = 0;
    // int temp;
    // for (int ik = 1; ik <= n; ik++) // ik is the size of matrix
    // {
    //     for (int in = 0; in < n-ik+1; in++) // for every row
    //     {
    //         int lo = 0, hi = m-ik, mid;
    //         temp = 0;
    //         while (lo <= hi) // Binary search
    //         {
    //             mid = (hi - lo)/2 + lo;
    //             ull pref = arr[in+ik][mid+ik] - arr[in][mid+ik] - arr[in+ik][mid] + arr[in][mid];
    //             //cout << "size:" << ik << "  row:" << in << "  mid:" << mid << " pref:" << pref << endl;
    //             if (pref >= (1ll*ik*ik*K))
    //             {
    //                 temp = m - mid - ik + 1;
    //                 hi = mid - 1;
    //             }
    //             else
    //             {
    //                 lo = mid + 1;
    //             }
    //         }
    //         res += temp;
    //     }
    // }// n*log(m) vs m*log(n)


    // TWO POINTER THING
    for (ull ik = 1; ik <= n; ik++) // size of sub-array
    {
        ll im = 0, in = n - ik;
        while ((im < m-ik+1) && (in >= 0))
        {
            ull pref = arr[in+ik][im+ik] - arr[in][im+ik] - arr[in+ik][im] + arr[in][im];
            if (pref >= ik*ik*K)
            {
                res += m - im - ik + 1;
                //debug2(in, im);
                //debug2(res, ik);
                in--;
            }
            else
            {
                im++;
            }
        }
    }
    cout << res;
    cout << "\n";
}


int main()
{
    file_i_o();
    i_am_speed();

    ll t = 1;
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