#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    string a, b;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> a >> b;
        bool flag = true;
        for(int i = 0; i < a.length(); i++){
            if(a[i] == '?' || b[i] == '?'){
                continue;
            }
            else if(a[i] != b[i]){
                flag = false;
            }
        }
        if (flag){cout<<"Yes\n";}
        else{cout<<"No\n";}
    }
    return 0;
}