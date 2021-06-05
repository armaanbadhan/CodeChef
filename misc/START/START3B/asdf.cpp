#include <bits/stdc++.h>
using namespace std;


int main()
{
    int n = 3, m = 3;
    vector <vector<int>> visited;
    vector <int> collections(m, 0);

    for (int im = 0; im < m; im++)
    {
        cout << collections[im] << " ";
    }
    cout << endl;


    for (int in = 0; in < n; in++)
    {
        cout << "vis size: " << visited.size() << endl;
        visited.push_back(collections);
    }
    
    cout << "vis size final: " << visited.size() << endl;
    for (int in = 0; in < n; in++)
    {
        for (int im = 0; im < m; im++)
        {
            cout << visited[in][im] << " " << in << " " << im << endl;
        }
        cout << endl;
    }
    return 0;
}
