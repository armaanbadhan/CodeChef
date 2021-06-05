#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    for(int it = 0; it < t; it++) {
        bool y = true;
        string s;
        cin >> s;
        int n = s.length();

        char char_arr[n];
        strcpy(char_arr, s.c_str());

        sort(char_arr, char_arr + (n/2));
        sort(char_arr + n - (n/2), char_arr + n);
 
        for (int i = 0; i < n/2; i++){
           if (char_arr[i] != char_arr[i + ((n+1)/2)]) {
               y = false;
               break;
           }
        }
        if (y) {cout << "YES\n";}
        else   {cout << "NO\n";}
    }
    return 0;
}