#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    string s;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n;
        cin >> s;
        int q = 0;
        for(int in=0;in<n;in++){
            if (s[in] == 'I'){
                q = 2;
                break;
            }
            else if(s[in]=='Y'){
                q = 1;
            }
        }
        if(q==2){cout << "INDIAN\n";}
        else if (q==1){cout << "NOT INDIAN\n";}
        else{cout << "NOT SURE\n";}
    }
    return 0;
}