#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);


bool isprime(int n)
{
    if (n < 2)return false;
    if (n < 4)return true;
    if (n%2==0)return false;
    if (n%3==0)return false;
    int i = 5, s = sqrt(n)+1;
    while (i <= s)
    {
        if (n%i == 0)return false;
        i += 2;
        if (n%i == 0)return false;
        i += 4;
    }
    return true;
}




void solve()
{
    int n, cnt = 0, res = 0, num = 2;
    cin >> n;
    while (cnt < n)
    {
        if (isprime(num))
        {
            cnt++;
            res += num;
        }
        num++;
    }
    
    cout << res;
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
