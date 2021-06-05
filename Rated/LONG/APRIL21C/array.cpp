#include<iostream>
using namespace std;

int main(){
    int arr[5]{3};
    arr[5] = 1;
    arr[8] = 7;
    for (int in = 0; in < 10; in++){
        cout << arr[in] << " ";
    }
    return 0;
}