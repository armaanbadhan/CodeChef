#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float x1, y;
    int x;
    cin >> x >> y;
    x1 = x;
    cout << fixed << setprecision(2);

    if (x1 + 0.5 <= y and x % 5 == 0) {
        cout << y - x1 - 0.5;
    }
    else {
        cout << y;
    }
}
