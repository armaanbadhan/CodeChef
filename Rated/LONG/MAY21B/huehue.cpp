#include<bits/stdc++.h>
using namespace std;

int main(){
    long long int n, x;
    cin>>n>>x;

    long long int arr[n];
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }
    long long int m = 1e9 + 7;
    long long int dp[x + 1];
    memset(dp, 0, x+1);
    dp[0] = 1;

    for(auto i : arr){
        for(long long int j = 1; j < x+1; j++){
            if (j - i >= 0){
                dp[j] = (dp[j] % m ) + (dp[j - i] % m);
                dp[j] %= m;
            }
        }
    }
    cout<<dp[x];
    return 0;
}