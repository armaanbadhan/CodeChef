#include <iostream>
#include <cmath>
#include <vector>
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
m%a%b = m%b%a
a < b
m%a <= a < b
m%a = m%b%a
--> m = b*(m/b) + m%b --> b*(m/b) = m - m%b
(b*(m/b) + m%b)%a = (m%b)%a
(b*(m/b))%a = 0
--> (m - m%b)%a = 0 //  to count the number of such pairs
2 cases -> m >= b, m < b

I) when m < b:
    m%b = m
    (m - m)%a = 0
    all possible values of a -> 
II) m <= b:
    find factors of m - m%b < b and add them to res
    pre-computation
ez
*/

ll factors(int n, int a)        // calculating for every takes time, pre-compute
{
    // calculates factors of n, scricly less than 'a'
    int s = sqrt(n);
    ll res = 0;
    for (int i = 1; i <= s; i++)
    {
        if ((n%i) == 0)
        {
            if (i < a)
            {
                res++;
            }
            if (n/i != i)
            {
                if (n/i < a)
                {
                    res++;
                }
            }
        }
    }
    return res;
}

const int MAXM = 5e5;
vector <vector <int>>vec;

void seive()
{

}




void solve()
{
    int n, m;
    cin >> n >> m;
    ll res = 0;
    for (int b = 2; b <= n; b++)
    {
        if (m < b)
        {
            res += b - 1;
        }
        else
        {
            res += factors(m - m%b, b);
        }
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