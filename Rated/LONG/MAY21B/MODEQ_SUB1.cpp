#include <iostream>
#include <vector>
using namespace std;

#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);
#define debug2(a, b) cout << a << " " << b << endl;
#define debug3(a, b, c) cout << a << " " << b << "  " << c << endl;

typedef long long ll;
typedef unsigned long long ull;

void file_i_o();

/*
ASCII VALUES 'A' -> 65, 'Z' -> 90, 'a' -> 96, 'z' -> 122, '0' -> 48;
INT_MAX -> 2,147,483,647 (10^10), LLONG_MAX -> 9,223,372,036,854,775,807 (10^19)
*///////////////////////////////////////////////////////////////////////////////


void solve()
{
    int n, m;
    cin >> n >> m;
    int res = 0;
    vector<int> arr;
    vector<int> brr;
    for (int b = 2; b <= n; b++)
    {
        for (int a = 1; a < b; a++)
        {
            if (((m%a)%b) == ((m%b)%a))
            {
                res++;
                //debug3(a, b, m%b);
                arr.push_back(a);
                brr.push_back(b);
            }
        }
    }
    for (int i = 0; i < arr.size(); i++)
    {
        //debug3(m%(arr[i]), m%(brr[i]), brr[i] % arr[i]);
        //debug2(arr[i], brr[i]);
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