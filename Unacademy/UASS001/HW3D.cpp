#include <bits/stdc++.h>
using namespace std;
#define i_am_speed() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

long long noofzero(int n){
    long long res = 0;
    while (true){
        n /= 5;
        res += n;
        if (n<5){
            return res;
        }
    }
}


int main(){
    i_am_speed();

    int n;
    cin >> n;
    int temp = n - n%5;
    while (noofzero(temp) < n){
        temp += 5;
    }
    if (noofzero(temp) != n){
        cout << "No solution";
    }
    else{
        cout << temp;
    }
    return 0;
}

// TLE
