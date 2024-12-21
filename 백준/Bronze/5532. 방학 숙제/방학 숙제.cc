#include <iostream>

using namespace std;

int main()
{
    int l,a,b,c,d;
    cin >> l >> a >> b >> c >> d;
    
    int t = max((a+c-1)/c,(b+d-1)/d);
    cout << l-t;
    
    return 0;
}