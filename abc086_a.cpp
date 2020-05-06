#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;

int main()
{
    int a, b;
    cin >> a >> b;
    cout << ((a * b) % 2 == 0 ? "Even" : "Odd") << endl;
    return 0;
}
