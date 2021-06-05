#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    string s;
    cin >> t;
    for(int it = 1; it <= t; it++) {
        cin >> s;
        if      (s == "b" or s == "B") {cout << "BattleShip\n";}
        else if (s == "c" or s == "C") {cout << "Cruiser\n";}
        else if (s == "d" or s == "D") {cout << "Destroyer\n";}
        else if (s == "f" or s == "F") {cout << "Frigate\n";}
    }
    return 0;
}