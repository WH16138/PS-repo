#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> cup(4);
    cup[1] = 1;

    int N,a,b;
    cin >> N;

    for (int i = 0; i<N;i++) {
        cin >>a >>b;
        swap(cup[a],cup[b]);
    }

    for (int i = 1; i<4; i++) {
        if (cup[i])
            cout << i << endl;
    }

    return 0;
}