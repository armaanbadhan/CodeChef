#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, ar[4];
    cin >> t;
    for(int it = 0; it < t; it++) {
        for(int in = 0; in < 4; in++){
            cin >> ar[in];
        }
        sort(ar, ar+4);

        if(ar[0]==ar[1] && ar[2]==ar[3]){cout<<"YES\n";}
        else{cout<<"NO\n";}
    }
    return 0;
}