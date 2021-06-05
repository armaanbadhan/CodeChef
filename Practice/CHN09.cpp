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
        int cnt_a = 0, cnt_b = 0;
        for(auto ch:s){
            if(ch=='a'){++cnt_a;}
            else{++cnt_b;}
        }
        if(cnt_b > cnt_a){cout<<cnt_a<<"\n";}
        else{cout<<cnt_b<<"\n";}
    }
    return 0;
}