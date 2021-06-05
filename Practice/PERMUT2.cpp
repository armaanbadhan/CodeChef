#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    jump:
    cin >> t;
    if (t){
        bool a = true;
        int ar[t+1], inv[t+1];
        for(int it = 1; it<=t; it++){cin >> ar[it];}
        for(int it = 1; it<=t; it++){inv[ar[it]]=it;}
        for(int it = 1; it<=t; it++){
            if (ar[it] != inv[it]){
                a = false;
                break;
            }
        }
        if (a){cout << "ambiguous\n";}
        else{cout << "not ambiguous\n";} // online judge dumb
        goto jump;
    }
    return 0;
}