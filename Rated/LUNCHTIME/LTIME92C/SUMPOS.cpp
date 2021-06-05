#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, a, b, c;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b >> c;
        if ( a+b==c or b+c== a or c+a == b){
            cout << "YES\n";
        }
        else{cout << "No\n";}

    }
    return 0;
}