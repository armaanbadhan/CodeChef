#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, b, c, diff;
    cin >> t;
    for(int it = 0; it < t; it++)
    {
        cin >> a >> b >> c;
        diff = abs(a-b);
        if (diff <= c)
        {
            cout << "0\n";
        }
        else
        {
            cout << diff - c << "\n";
        }
    }
    return 0;
}