#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n, e = 0, o = 0;
    cin >> t;
    for(int it = 0; it < t;it++) {
        cin >> n;
        if (n & 1){
            o += 1;
        }
        else{
            e += 1;
        }

    }
    if (e > o){
        cout << "READY FOR BATTLE\n";
    }
    else{
        cout << "NOT READY\n";
    }
    return 0;
}