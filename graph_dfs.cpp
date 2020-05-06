#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define rep(i, n) for (int i = 0; i < n; ++i)
using ll = long long int;
using graph = vector<vector<int>>;

int main()
{
    int n, m;
    cin >> n >> m;

    graph g(n);
    rep(i, m)
    {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
    }
    print(g);
    return 0;
}
