#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while (t--)
	{
	    int n, k;
	    cin >> n >> k;
	    int men = 0;
	    int temp, cnt = 1;
	    for (int in = 0; in < n; in++)
	    {
	        cin >> temp;
	        if (temp == 0)
	        {
	            cnt++;
	        }
	        else
	        {
	            men += (cnt-1)/2;
	            cnt = 0;
	        }
	    }
	    men += (cnt-1)/2;
	    cout << ((men >= k) ? 1 : 0) << "\n";
	}
	return 0;
}

// 80 pts
