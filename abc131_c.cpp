#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;
#define rep(i, n) for (int i = 0; i < n; ++i)
typedef long long int int64;

int64 gcd(int64 a, int64 b)
{
    return b ? gcd(b, a % b) : a;
}

int64 num(int64 a, int64 b, int64 c)
{
    int64 g = gcd(b, c);
    int64 l = b / g * c;
    return n - n / b - n / c + n / l;
}
