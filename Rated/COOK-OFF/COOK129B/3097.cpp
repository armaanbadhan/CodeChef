#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int a, k;
    cin >> a >> k;
    long long int org = a;
    vector<int> v;
    int cnt = 0;
    while(org)
    {
        int y = org % 10;
        cnt += 1;
        v.push_back(y);
        org /= 10;
    }
    
    for(int i = cnt - 1; i > 0; i--)
    {
        if (k)
        {
            if(v[i - 1] > v[i])
            {
                int temp = v[i];
                v[i] = v[i - 1];
                v[i - 1] = temp;
                k -= 1;
            }
        }
    }
    for(int i = cnt - 1; i >= 0; i--)
    {
        cout<<v[i];
    }
    return 0;
}
