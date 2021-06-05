#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
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


// O(T * (n + f + f)) too high :heh:
// void solve()
// {
//     int n, k, f;
//     cin >> n >> k >> f;
//     int arr[f+1] = {0};
//     int enter, exit;
//     for (int in = 0; in < n; in++)
//     {
//         cin >> enter >> exit;
//         arr[enter]++;
//         arr[exit]--;
//     }
//     for (int i = 1; i <= f; i++)
//     {
//         arr[i] += arr[i-1];
//     }
//     int got = 0;
//     for (int i = 0; i <= f; i++)
//     {
//         if (arr[i] == 0)
//         {
//             got++;
//         }
//     }
//     cout << ((got >= k) ? "YES" : "NO");
//     cout << "\n";
// }


void solve()
{
    int n, k, f;
    cin >> n >> k >> f;
    
    vector<pair<int, int>> vec;
    int enter, exit;
    for (int in = 0; in < n; in++)
    {
        cin >> enter >> exit;
        vec.push_back(make_pair(enter, exit));
    }
    sort(vec.begin(), vec.end());
    // https://github.com/armaanbadhan/CodeChef/blob/main/Unacademy/INPRG01/MXOVRLP4.py
    // https://github.com/armaanbadhan/CodeChef/blob/main/Unacademy/INPRG01/MXOVRLP3.py
    // https://www.codechef.com/START4B/problems/CTIME
    
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
