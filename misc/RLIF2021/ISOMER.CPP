#include <iostream>
using namespace std;

const int arr[] = {0, 1, 1, 1, 2, 3, 5, 9, 18, 35, 75, 159, 355, 802, 1858, 4347, 10359, 24894, 60523, 148284, 366319};


int main() {
	// your code goes here
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
	int t; cin >> t;
	while (t--)
	{
	    int n; cin >> n;
	    cout << arr[n] << "\n";
	}
	return 0;
}
