#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    char input, v[5] = {'A', 'E', 'I', 'O', 'U'};
    cin >> input;
    bool flag = false;
    for(int i = 0;i<5;i++){
        if(input==v[i]){
            flag=true;
            break;
        }
    }
    if(flag){cout<<"Vowel";}
    else{cout<<"Consonant";}
    return 0;
}