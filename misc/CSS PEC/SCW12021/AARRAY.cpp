#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n; cin >> n;
	int inp[n], sorted[n], temp;
	for(int in = 0; in < n; in++)
	{
	    cin >> temp;
	    inp[in] = temp;
	    sorted[in] = temp;
	}
	sort(sorted, sorted + n);
	int start = -1, end = -1;
	bool started = false;
	for(int in = 0; in < n; in++)
	{
	    if(inp[in] != sorted[in])
	    {
	        if (!started)
	        {
	            start = in+1;
	            started = true;
	        }
	        end = in+1;
	    }
	}
	if (started)
	{
	    cout << start << " " << end << endl;
	}
	else
	{
	    cout << -1 << endl;
	}
	return 0;
}

// AC
