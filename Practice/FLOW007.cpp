#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    int temp = n;
    int ans = 0;
    while (n) {
        ans = (ans * 10) + (n % 10);
        n = n / 10;
    }
    if (ans == temp) {cout << "YES";}
    else {cout << "NO";}
    return 0;
}    