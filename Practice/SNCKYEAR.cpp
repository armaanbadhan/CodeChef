#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n, snk[5] = {2010, 2015, 2016, 2017, 2019};
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n;
        bool flag = false;
        for(int in = 0;in < 5;in++){
            if (n == snk[in]){
                flag = true;
                break;
            }
        }
        if(flag){cout<<"HOSTED\n";}
        else{cout<<"NOT HOSTED\n";}
    }
    return 0;
}