#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int t;
    cin >> t;
    jump:
    while (t--){
        int n, j, i = 2;
        cin >> n;
        j = sqrt(n);
        if (n == 1){
            cout << "no\n";
            continue;
        }
        while (i <= j){
            if (n % i == 0){
                cout << "no\n";
                goto jump;
            }
            i++;
        }
        cout << "yes\n";
    }

}