#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        int number;
        int sum = 0;
        cin >> number;

        while(number){
            sum += (number % 10);
            number = number/10;
        }
        cout << sum << endl;
    }
}