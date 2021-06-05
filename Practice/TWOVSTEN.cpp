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
        if((n%5)==0){
            if((n%10)==0){
                cout << "0\n";
            }
            else{
                cout << "1\n";
            }
        }
        else{cout << "-1\n";}
        
    }
    return 0;
}