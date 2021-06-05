#include <iostream>
using namespace std;

#define MOD 1000000007
#define i_am_speed() ios_base::sync_with_stdio(false);\
                     cin.tie(NULL);\
                     cout.tie(NULL);
#define debug2(a, b) cout << a << " " << b << endl;

typedef long long ll;
typedef unsigned long long ull;

void file_i_o();

/*
ASCII VALUES 'A' -> 65, 'Z' -> 90, 'a' -> 96, 'z' -> 122, '0' -> 48;
INT_MAX -> 2,147,483,647 (10^10), LLONG_MAX -> 9,223,372,036,854,775,807 (10^19)
*///////////////////////////////////////////////////////////////////////////////


char arr[3][3];


int* checkDiagonals()
{
    int res1 = 0, res2 = 0;
    if ((arr[0][0] == arr[1][1]) && (arr[1][1] == arr[2][2]))
    {
        if (arr[1][1] == 'X')res1++;
        if (arr[1][1] == 'O')res2++;
    }
    if ((arr[2][0] == arr[1][1]) && (arr[1][1] == arr[0][2]))
    {
        if (arr[1][1] == 'X')res1++;
        if (arr[1][1] == 'O')res2++;
    }
    int* dia = new int[2];
    dia[0] = res1;
    dia[1] = res2;
    return dia;
}


int* horizontal()
{
    int res1 = 0, res2 = 0;
    for(int i = 0; i < 3; i++)
    {
        if((arr[i][0] == arr[i][1]) && (arr[i][1] == arr[i][2]))
        {
            if (arr[i][0] == 'X')res1++;
            if (arr[i][0] == 'O')res2++;
        }
    }
    int* hor = new int[2];
    hor[0] = res1;
    hor[1] = res2;
    return hor;
}


int* verticle()
{
    int res1 = 0, res2 = 0;
    for(int i = 0; i < 3; i++)
    {
        if((arr[0][i] == arr[1][i]) && (arr[1][i] == arr[2][i]))
        {
            if (arr[0][i] == 'X')res1++;
            if (arr[0][i] == 'O')res2++;
        }
    }
    int* ver = new int[2];
    ver[0] = res1;
    ver[1] = res2;
    return ver;
}

/*

OOO
XX_
XX_

ans -> 1
expected -> 3
*/

void solve()
{
    int empty = 0, xx = 0, oo = 0;
    char ch;

    //////////////////////////////////
    //int n;
    //cin >> n;
    ///////////////remember to comment
    
    for(int i = 0; i < 3; i++)
    {
        for(int j =0; j < 3; j++)
        {
            cin >> ch;
            arr[i][j] = ch;
            if (ch == '_')empty++;
            if (ch == 'X')xx++;
            if (ch == 'O')oo++;
        }
    }
    
    int dxx = checkDiagonals()[0], doo = checkDiagonals()[1];
    int hxx = horizontal()[0], hoo = horizontal()[1];
    int vxx = verticle()[0], voo = verticle()[1];

    // debug2(dxx, doo);
    // debug2(hxx, hoo);
    // debug2(vxx, voo);

    if ((xx == oo) || (xx - oo == 1)){}
    else
    {
        cout << 3 << endl;
        return;
    }

    bool foundxx = dxx + hxx + vxx > 0;
    bool foundoo = doo + hoo + voo > 0;

    //        T              &&           T
    if (foundxx && foundoo)
    {
        cout << 3 << endl;
        return;
    }

    if (hxx > 1 || vxx > 1 || hoo > 1 || voo > 1)
    {
        cout << 3 << endl;
        return;
    }

    //         F               &&           F
    if ((dxx + hxx + vxx == 0) && (doo + hoo + voo == 0))
    {
        if(empty == 0)
        {
            // draw
            cout << 1 << endl;
            return;
        }
        else
        {
            // no winner, but can move
            cout << 2 << endl;
            return;
        }
    }

    if (dxx + hxx + vxx > 0)
    {
        if (xx == oo + 1)
        {
            cout << 1 << endl;
            return;
        }
        else
        {
            cout << 3 << endl;
            return;
        }
    }

    // else
    else if (doo + hoo + voo > 0)
    {
        if (oo == xx)
        {
            cout << 1 << endl;
            return;
        }
        else
        {
            cout << 3 << endl;
            return;
        }
    }
}


int main()
{
    file_i_o();
    i_am_speed();

    int t = 1;
    cin >> t;
    for(int it = 0; it < t; it++)
    {
        solve();
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