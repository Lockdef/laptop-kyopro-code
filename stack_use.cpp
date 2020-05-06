#include <bits/stdc++.h>
using namespace std;

int main()
{
    stack<int> S;

    S.push(3);
    S.push(7);
    S.push(1);

    cout << S.size() << " ";
    S.pop();
    cout << S.size() << " ";
    S.pop();
    cout << S.size() << " ";
    S.pop();
    cout << S.size() << endl;
    S.pop();
    return 0;
}
