#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
#define fast() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define int long long

int mn1(string s,int p){
    int f[27]{0};
    int j=p+1;
    int n = s.length();
    for(int i=j;i<n;i++){
        f[s[i]-'a']++;
    }
    int flag=1;
    int temp[27]{0};
    for(int i=0;i<p;i++){
        temp[s[i]-'a']++;
    }
    for(int i=0;i<27;i++){
        if(temp[i]!=f[i]){flag=0;}
    }
    if(flag){
        return 0;
    }
    int total = 0;
    for(int i=0;i<27;i++){
        if(temp[i]>f[i]){
            total+=(temp[i]-f[i]);
        }
        else if(temp[i]<f[i]){
            total+=(f[i]-temp[i]);
        }
    }
    return total;
}

int mn2(string s,int p){
    int f[27]{0};
    int j=p+2;
    int n = s.length();
    for(int i=j;i<n;i++){
        f[s[i]-'a']++;
    }
    int flag=1;
    int temp[27]{0};
    for(int i=0;i<p;i++){
        temp[s[i]-'a']++;
    }
    for(int i=0;i<27;i++){
        if(temp[i]!=f[i]){flag=0;}
    }
    if(flag){
        return 0;
    }
    int total = 0;
    for(int i=0;i<27;i++){
        if(temp[i]>f[i]){
            total+=(temp[i]-f[i]);
    }
        else if(temp[i]<f[i]){
            total+=(f[i]-temp[i]);
        }
    }
    return total;
}

void solve(){
    string s;int p;
    cin>>s>>p;
    int n = s.length();
    p--;
    int mon1=INT_MAX,mon2=INT_MAX;
    mon1 = mn1(s,p);
    if(p+1<n and s[p]==s[p+1]){
        mon2 = mn2(s,p);
    }
    // cout<<mon1<<" "<<mon2<<endl;
    cout<<min(mon1,mon2);
}

signed main(){
    fast();
    int t = 1;
    cin >> t;
    int ar = 1;
    while (ar <= t){
        solve();
        cout << endl;
        ar++;
    }
    return 0;
}
