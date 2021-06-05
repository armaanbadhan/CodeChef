#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n;
        int temp = n, rev = 0;
        while (temp) {
            rev = (rev*10) + (temp%10);
            temp = temp / 10;
        }
        if (rev == n) {cout << "wins\n";}
        else          {cout << "loses\n";}
    }
    return 0;
}