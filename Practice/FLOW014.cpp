#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, c;
    double b;
    cin >> t;
    while (t--) {
        cin >> a >> b >> c;
        bool aa = a > 50, bb = b < 0.7, cc = c > 5600;

        if (aa && bb && cc)    {cout << 10 << "\n";}
        else if(aa && bb)      {cout << 9 << "\n";}
        else if(bb && cc)      {cout << 8 << "\n";}
        else if(aa && cc)      {cout << 7 << "\n";}
        else if(aa || bb || cc){cout << 6 << "\n";}
        else                   {cout << 5 << "\n";}
    }
    return 0;
}