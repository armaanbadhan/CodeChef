#include <iostream>
using namespace std;

int main(){
    int n = 3, m = 3;
    int arr[n+1][m+1];

    for (int im = 0; im <= m; im++){
        arr[0][im] = 0;
    }

    for (int in = 1; in <= n; in++){
        arr[in][0] = 0;
        for (int im = 1; im <= m; im++){
            cin >> arr[in][im];
        }
    }

    for (int in = 0; in <= n; in++){
        for (int im = 0; im <= m; im++){
            cout << arr[in][im] << " ";
        }
        cout << endl;
    }
    return 0;
}
