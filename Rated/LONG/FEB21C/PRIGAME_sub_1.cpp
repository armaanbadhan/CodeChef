#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, x, y;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> x >> y;
        if(x==1 || x==2){cout << "Chef\n";}
        else{cout << "Divyam\n";}
    }
    return 0;
}
// for subtask 1
// y == 1
// goldbach conjecture?