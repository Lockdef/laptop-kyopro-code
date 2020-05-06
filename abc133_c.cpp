#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;
#define rep(i, n) for (int i = 0; i < n; ++i)

int main()
{
    long long int l, r;
    cin >> l >> r;

    long long int ans = 2018;

    if (r - l >= 2019)
    {
        print(0);
        return 0;
    }
    else
    {
        for (long long int i = l; i < r; ++i)
        {
            for (long long int j = i + 1; j <= r; ++j)
            {
                ans = min(ans, (i * j) % 2019);
            }
        }
    }

    print(ans);

    return 0;
}
