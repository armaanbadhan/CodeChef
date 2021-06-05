#include <iostream>
using namespace std;

int main(){
    int t;
    while (true) {
        cin >> t;
        if (t == 42) {
            goto over;
        }
        cout << t << "\n";
    }
    over:
    return 0;
}