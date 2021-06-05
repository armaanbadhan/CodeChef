#include <bits/stdc++.h>
using namespace std;

double dist(int qw, int er, int ty, int ui){
    return sqrt((qw-ty)*(qw-ty) + (er-ui)*(er-ui));
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, z, x, c, v, b, n;
    double k;
    cin >> t;
    for(int it = 0; it < t; it++) {
        cin >> k >> z >> x >> c >> v >> b >> n;
        if( dist(z, x, c, v)<=k || dist(c, v, b, n)<=k || dist(b, n, z, x)>k ){
            cout << "yes\n";
        }
        else{cout << "no\n";}
        co///ut << dist(z, x, c, v) << "   " << dist(c, v, b, n) << "     " << dist(b, n, z, x);
    }
    return 0;
}//////////////////