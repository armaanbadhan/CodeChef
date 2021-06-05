#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n, a, b, c;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n;
        int arr[n];
        for(int in = 0; in < n; in++){
            cin >> arr[in];
        }
        sort(arr, arr+n);
        cout << 2*arr[n-1] - 2*arr[0] << "\n";
    }
    return 0;
}
// gave WA but same code in python gave AC lol