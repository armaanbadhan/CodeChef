#include <iostream>
using namespace std;


void addone(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        arr[i] += 1;
    }
}


int main()
{
    int n; cin >> n;
    int arr[n];
    for (int in = 0; in < n; in++)
    {
        cin >> arr[in];
    }
    addone(arr, n);
    for (int in = 0; in < n; in++)
    {
        cout << arr[in] << " ";
    }
    return 0;
}
