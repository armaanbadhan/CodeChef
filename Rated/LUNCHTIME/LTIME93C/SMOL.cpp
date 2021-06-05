#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n, k;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n >> k;
        if (k==0){cout<<n<<'\n';}
        else{cout<<n%k<<'\n';}
    }
    return 0;
}