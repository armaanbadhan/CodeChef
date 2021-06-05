#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    string s;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> s;
        int zero = 0, one = 0;
        for(auto ch:s){
            if(ch=='0'){
                ++zero;
            }
            else{
                ++one;
            }
        }
        if(one==1 || zero==1){
            cout<<"Yes\n";
        }
        else{
            cout << "No\n";
        }

    }
    return 0;
}