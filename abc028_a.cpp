#include <bits/stdc++.h>
using namespace std;
#define print(x) cout << x << endl;
#define input(x) cin >> x;

int main()
{
    int N;
    input(N);
    if (N < 60)
    {
        print("Bad");
    }
    else if (N < 90)
    {
        print("Good");
    }
    else if (N < 100)
    {
        print("Great");
    }
    else
    {
        print("Perfect");
    }
    return 0;
}
