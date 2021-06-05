#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);

using namespace std;
// i -> row number
// j -> column number
// n -> number of rows
// m -> number of columns
// li -> input list
// visited -> visiting check
// result -> groups of 1
void file_i_o();

// vector <vector<int>> visited;
vector <string> li(0);
vector <int> result;


void land_sizes(int i, int j, int n, int m, int &cnt)
{
    if (i >= n || i < 0 || j < 0 || j >= m)return;
    if (li[i][j] == '0')return;
    li[i][j] = '0';
    cnt++;
    land_sizes(i-1, j, n, m, cnt);
    land_sizes(i, j-1, n, m, cnt);
    land_sizes(i+1, j, n, m, cnt);
    land_sizes(i, j+1, n, m, cnt);    
}


void solve()
{
    int n, m;
    cin >> n >> m;
    
    li.resize(0);
    result.resize(0);

    //input
    for (int in = 0; in < n; in++)
    {
        string s;
        cin >> s;
        li.push_back(s);
    }

    // // set vis to 0 and push back
    // visited.resize(0);
    // vector <int> collections(m, 0);
    // for (int in = 0; in < n; in++)
    // {
    //     visited.push_back(collections);
    // }
    
    for (int in = 0; in < n; in++)
    {
        for (int im = 0; im < m; im++)
        {
            if (li[in][im] == '1')
            {
                int temp = 0;
                land_sizes(in, im, n, m, temp);
                result.push_back(temp);
            }
        }
    }

    sort(result.begin(), result.end(), greater<int>());
    
    // cout << "vis size: " << visited.size() << endl;
    // for (int in = 0; in < n; in++)
    // {
    //     for (int im = 0; im < m; im++)
    //     {
    //         cout << li[in][im] << " ";
    //     }
    //     cout << endl;
    // }

    int sum = 0;
    //cout << "size result: " << result.size() << endl;
    for(int i = 0; i < result.size(); i++)
    {
        if (i&1)
        {
            sum += result[i];
        }
    }
    cout << sum << endl;
}




int main()
{
    file_i_o();
    i_am_speed();

    int t;
    cin >> t;
    for (int it = 0; it < t; it++)
    {
        solve();
    }
    return 0;
}

void file_i_o()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
        freopen("error.txt", "w", stderr);
    #endif
}
