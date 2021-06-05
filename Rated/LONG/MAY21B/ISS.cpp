#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <unordered_map>
using namespace std;

#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);
#define debug2(a, b) cout << a << " " << b << endl;

typedef long long ll;
typedef unsigned long long ull;

void file_i_o();

/*
ASCII VALUES 'A' -> 65, 'Z' -> 90, 'a' -> 96, 'z' -> 122, '0' -> 48;
INT_MAX -> 2,147,483,647 (10^10), LLONG_MAX -> 9,223,372,036,854,775,807 (10^19)
*///////////////////////////////////////////////////////////////////////////////


bool isPrime(int n)
{
    if (n < 2)return false;
    if (n < 4)return true;
    if ((n&1) == 0)return false;
    if ((n%3) == 0)return false;
    int i = 5, s = sqrt(n);
    while (i <= s)
    {
        if ((n%i) == 0)return false;
        i += 2;
        if ((n%i) == 0)return false;
        i += 4;
    }
    return false;
}


void solve()
{
    int k;
    cin >> k;

    ull num = __gcd(4*k*k + 5*k + 1, k + 4*k*k);
    if (isPrime(num))
    {
        cout << num + 2*k - 1;
        return;
    }

    vector<ull> arr;
    for (int ik = 1; ik <= 2*k + 1; ik++)
    {
        arr.push_back(k + ik*ik);
    }

    vector<ull> gcds;
    unordered_map<int, int> dict;
    ull res = 0;
    int temp;

    for (int i = 0; i < 2*k; i++)
    {
        temp = __gcd(arr[i], arr[i+1]);
        gcds.push_back(temp);
        if (dict.find(temp) == dict.end())
        {
            dict[temp] = 1;
        }
        else
        {
            dict[temp] += 1;
        }

        res += __gcd(arr[i], arr[i+1]);
    }
    // for (int i = 0; i < 2*k; i++)
    // {
    //     cout << gcds[i] << " ";
    // }
    // cout << endl;
    for (auto i = dict.begin(); i != dict.end(); i++)
    {
        cout << i->first << " " << i->second << endl;
    }
    // for (int ik = 0; ik < 2*k + 1; ik++)
    // {
    //     cout << arr[ik] << " ";
    // }
    // debug2(arr[2*k], arr[2*k - 1]);
    // debug2(k + (2*k + 1)*(2*k + 1), k + 2*k*2*k);

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