#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

using namespace std;

typedef complex<double> cpx;
const double PI = acos(-1);

void fft(vector<cpx>& a, bool inverse) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        while (j & bit) {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        double angle = 2 * PI / len * (inverse ? -1 : 1);
        cpx wlen(cos(angle), sin(angle));
        for (int i = 0; i < n; i += len) {
            cpx w(1);
            for (int j = 0; j < len / 2; j++) {
                cpx u = a[i + j], v = a[i + j + len / 2] * w;
                a[i + j] = u + v;
                a[i + j + len / 2] = u - v;
                w *= wlen;
            }
        }
    }
    if (inverse) {
        for (auto& x : a) x /= n;
    }
}

vector<double> convolution(const vector<int>& a, const vector<int>& b) {
    int n = 1;
    while (n < a.size() + b.size()) n <<= 1;

    vector<cpx> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    fa.resize(n);
    fb.resize(n);

    fft(fa, false);
    fft(fb, false);

    for (int i = 0; i < n; i++) {
        fa[i] *= fb[i];
    }

    fft(fa, true);

    vector<double> result(n);
    for (int i = 0; i < n; i++) {
        result[i] = fa[i].real();
    }
    return result;
}

int main() {
    int n;
    cin >> n;

    vector<int> x(n), y(n);
    for (int i = 0; i < n; i++) cin >> x[i];
    for (int i = 0; i < n; i++) cin >> y[i];

    vector<int> extended_x(2 * n);
    for (int i = 0; i < n; i++) {
        extended_x[i] = x[i];
        extended_x[i + n] = x[i];
    }

    reverse(y.begin(), y.end());
    
    vector<double> conv_result = convolution(extended_x, y);

    double max_result = 0;
    for (int i = n - 1; i < 2 * n - 1; i++) {
        max_result = max(max_result, conv_result[i]);
    }

    cout << static_cast<int>(round(max_result)) << endl;

    return 0;
}
