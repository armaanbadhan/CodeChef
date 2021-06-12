#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int t; cin >> t;
	while (t--)
	{
	    string s; cin >> s;
	    int g=0, o=0, l=0, e = 0;
	    for (char ch: s)
	    {
	        if (ch == 'g')g++;
	        if (ch == 'o')o++;
	        if (ch == 'l')l++;
	        if (ch == 'e')e++;
	    }
	    cout << min(min(g/2, o/2), min(l, e)) << endl;
	}
	return 0;
}

// AC
