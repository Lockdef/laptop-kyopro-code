#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;
#define rep(i, n) for (int i = 0; i < n; ++i)
typedef long long int ll;

int main()
{
    ll a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;
    ll num[5] = {a, b, c, d, e};

    vector<int> v;

    for (ll i = 0; i < 3; ++i)
    {
        for (ll j = i + 1; j < 4; ++j)
        {
            for (ll k = j + 1; k < 5; ++k)
            {
                v.push_back(num[i] + num[j] + num[k]);
            }
        }
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    print(v[v.size() - 3]);

    return 0;
}
