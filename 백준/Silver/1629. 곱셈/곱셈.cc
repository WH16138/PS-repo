#include <iostream>

using namespace std;

int main() {
    long long a,b,c;
    long long A = 1;
    cin >> a >> b >> c;
    while (b > 0) {
        if (b%2) {
            A *= a;
            b -= 1;
        }
        else {
            a *= a;
            b /= 2;
        }
        a %= c;
        A %= c;
    }
    cout << A;
}