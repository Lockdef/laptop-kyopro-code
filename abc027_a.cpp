#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;

int main()
{
    int l[3];
    for (int i = 0; i < 3; ++i)
        input(l[i]);
    if (l[0] == l[1])
    {
        print(l[2])
    }
    else if (l[0] == l[2])
    {
        print(l[1])
    }
    else
    {
        print(l[0])
    }
    return 0;
}
