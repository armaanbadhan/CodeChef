#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	string s;
	ll n, k, t, i, j, p, ans;

	cin>>t;
	while(t--){
		cin>>s>>p;
		n = s.length();
		vector<int>arr(130,0);


		for(i = p; i < n; i++){
			arr[s[i]]++;
        }
		for(i = 0; i < p-1; i++){
			arr[s[i]]--;
        }

		j=0;
		for(i = 0; i < 127; i++){
			j += abs(arr[i]);
            cout << arr[i] << " ";
        }
        cout << "\n";

		k = arr[s[p-1]];
        cout << s[p-1] << "\n" << (p<n) << "\n" << (p<n && s[p-1]) << "\n" << s[p];
		if(p<n && s[p-1] == s[p]){
			j = min(j, j + abs(k-1) - abs(k));
        }
		cout << j << "\n";
	}
	return 0;
}