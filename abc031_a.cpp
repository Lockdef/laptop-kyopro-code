#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;

int main()
{
    int A, D;
    input(A);
    input(D);
    cout << ((A + 1) * D > A * (D + 1) ? (A + 1) * D : A * (D + 1)) << endl;

    return 0;
}
