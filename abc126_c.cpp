#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl
#define rep(i, n) for (int i = 0; i < n; ++i)
typedef long long int ll;

long double f(ll n, ll a, ll k)
{

    ll c = 0;
    while (a < k)
    {
        a *= 2;
        c++;
    }

    return (1.L / n) * pow(0.5, c);
}

int main()
{
    ll n, k;
    cin >> n >> k;
    long double r = 0;
    for (int i = 1; i < n + 1; i++)
    {
        r += f(n, i, k);
    }
    printf("%.12Lf\n", r);

    return 0;
}
