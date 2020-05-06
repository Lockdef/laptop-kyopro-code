#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;

int main()
{
    char s[3];
    cin >> s;
    int c = 0;
    for (int i = 0; i < 3; ++i)
    {
        if (s[i] == '1')
            c++;
    }
    cout << c << endl;
    return 0;
}
