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
        int a=n-1;
        int lr=a/4-a/100+a/400; 
        int w =(a+ lr)%7 + 1; 
        // int c = n/100;
        // int y = n%100 - 1;
        // int w = (29 -2*c + y + y/4 + c/4) % 7;
        if (w==6){cout<<"saturday\n";}
        if (w==0){cout<<"sunday\n";}
        if (w==1){cout<<"monday\n";}
        if (w==2){cout<<"tuesday\n";}
        if (w==3){cout<<"wednesday\n";}
        if (w==4){cout<<"thursday\n";}
        if (w==5){cout<<"friday\n";}
    }
    return 0;
}