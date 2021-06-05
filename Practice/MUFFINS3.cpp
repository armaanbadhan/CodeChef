#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    cin >> t;
    for(int it = 0; it < t;) {
        cin >> n;
        cout << n/2 + 1 << "\n";
        it++;
    }
    return 0;
}