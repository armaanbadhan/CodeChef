#include <iostream>
using namespace std;

int main() {
    int total;
    cin >> total;
    while (total--) {
        int a, b;
        cin >> a >> b;
        cout << ((1ll*a*b) + 1)/2 << endl;                      // ans would be ab/2 if both even or 1 even 1 odd
    }                                                           // if both odd ans = (ab+1)/2
    return 0;
}

// https://www.codechef.com/problems/EVENPSUM
