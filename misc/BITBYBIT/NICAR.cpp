#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    long long nicar[t], max = 0;
    for(int it = 0; it < t;) {
        cin >> nicar[it];
        it++;
    }

    for(int jt = 0; jt < t;) {
        cout << nicar[jt] + max;
        if (nicar[jt] + max > max) {
            max += nicar[jt];
        }
        jt++;
    }
    return 0;
}