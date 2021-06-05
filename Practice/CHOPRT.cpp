#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, b;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b;
        if      (a > b){cout << ">\n";}
        else if (b > a){cout << "<\n";}
        else           {cout << "=\n";}
    }
    return 0;
}