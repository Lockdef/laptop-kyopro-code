#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;
#define rep(i, n) for (int i = 0; i < n; ++i)
typedef long long int ll;

int main()
{
    ll n;
    input(n);
    print((n / 10) * 100 + ((n % 10) < 7 ? (n % 10) * 15 : 100));
    return 0;
}
