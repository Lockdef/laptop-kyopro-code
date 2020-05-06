#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;
#define rep(i, n) for (int i = 0; i < n; ++i)

int main()
{
    float A[4];
    rep(i, 4) input(A[i]);
    float r = A[1] / A[0] - A[3] / A[2];
    if (r == 0)
    {
        print("DRAW")
    }
    else if (r > 0)
    {
        print("TAKAHASHI");
    }
    else
    {
        print("AOKI");
    }
    return 0;
}
