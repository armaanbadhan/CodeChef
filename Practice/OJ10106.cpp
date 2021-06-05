#include <iostream>
using namespace std;

#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);
#define debug(a) cout << a << endl
#define debug2(a, b) cout << a << " " << b << endl;

typedef long long ll;
typedef unsigned long long ull;

void file_i_o();

/*
ASCII VALUES 'A' -> 65, 'Z' -> 90, 'a' -> 96, 'z' -> 122, '0' -> 48;
INT_MAX -> 2,147,483,647 (10^10), LLONG_MAX -> 9,223,372,036,854,775,807 (10^19)
*///////////////////////////////////////////////////////////////////////////////

/*

*/

void solve(string a, string b)
{
    int arr[501] = {0};
    int len = a.length();
    for (int i = 0; i < len; i++)
    {
        arr[i] = a[i - '0'];
    }
    for (int j = 0; j < len; j++)
    {
        int k = 0;
        int carry = 0;
        for (int k = 0; k < len; k++)
        {
            int num = (b[j] - '0')*arr[k] + carry;
            arr[k] = num%10;
            carry = num/10;
        }
        while (carry)
        {
            arr[len] += carry%10;
            carry /= 10;
            len++;
        }
    }
    for (int i = len; i >= 0; --i)cout << arr[i];
    cout << "\n";
}


int main()
{
    //file_i_o();
    i_am_speed();

    string a, b;

    while (cin >> a)
    {
        cin >> b;
        solve(a, b);
    }
    return 0;
}


void file_i_o()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
}