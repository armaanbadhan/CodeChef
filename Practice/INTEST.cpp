// A fast IO program 
#include <bits/stdc++.h> 
using namespace std; 

int main() { 
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL); 
	
	int n, k, t, sol = 0;
	cin >> n >> k; 
	while (n--) { 
		cin >> t; 
		if (t % k == 0){ 
			sol++;
        }
	}
	cout << sol; 
	return 0; 
}