#include <bits/stdc++.h>
using namespace std;
#define i_am_speed() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);


int main(){
    i_am_speed()
    int t, n;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> n;
        int arr[n] = {}, ans = 0;
        for(int in = 0; in<n; in++){
            cin >> arr[in];
        }

        for(int i = 0; i<n; i++){        //starting point
            for (int j = i; j<n; j++){   //end point
                long long sum = 0, prod = 1; 
                for (int k = i; k<=j;k++){
                    sum += arr[k];
                    prod *= arr[k];
                }
                if(sum==prod)++ans;
            }
        }
        cout << ans << '\n';
    }
    return 0;
}