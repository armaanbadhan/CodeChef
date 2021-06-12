#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	// your code goes here
	int n, k;
	cin >> n;
	int arr[n];
	for (int in = 0; in < n; in++)
	{
	    cin >> arr[in];
	}
	cin >> k;
	int ik = 0;
	while (true)
	{
	    sort(arr+ik, arr+ min(ik+k, n));
	    ik += k;
	    if (ik > n)break;
	    sort(arr+ik, arr+ min(ik+k, n), greater<int>());
	    ik += k;
	    if (ik > n)break;
	}
	
	for (int in = 0; in < n; in++)
	{
	    cout << arr[in] << " ";
	}
	cout << endl;
	return 0;
}

// AC
