#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

using namespace std;

const double PI = acos(-1);
typedef complex<double> cpx;

void fft(vector<cpx>& a, bool inverse) {
    int n = a.size();

    for (int i = 0; i < n; i++) {
        int rev = 0;
        for (int j = 1, target = i; j < n; j <<= 1, target >>= 1) {
            rev = (rev << 1) + (target & 1);
        }
        if (i < rev) {
            swap(a[i], a[rev]);
        }
    }

    for (int len = 2; len <= n; len <<= 1) {
        double x = 2 * PI / len * (inverse ? -1 : 1);
        cpx diff(cos(x), sin(x));
        for (int i = 0; i < n; i += len) {
            cpx e(1);
            for (int j = 0; j < len / 2; j++) {
                int cur = i + j;
                cpx even = a[cur];
                cpx oddE = a[cur + len / 2] * e;
                a[cur] = even + oddE;
                a[cur + len / 2] = even - oddE;
                e *= diff;
            }
        }
    }

    if (inverse) {
        for (int i = 0; i < n; i++) {
            a[i] /= n;
        }
    }
}

vector<int> multiply(const vector<int>& a, const vector<int>& b) {
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

    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        result[i] = round(fa[i].real());
    }

    return result;
}

int main() {
    string x, y;
    cin >> x >> y;

    vector<int> a(x.size()), b(y.size());
    for (size_t i = 0; i < x.size(); i++) {
        a[i] = x[x.size() - 1 - i] - '0';
    }
    for (size_t i = 0; i < y.size(); i++) {
        b[i] = y[y.size() - 1 - i] - '0';
    }

    vector<int> result = multiply(a, b);

    for (int i = 0; i < result.size(); i++) {
        if (result[i] >= 10 && i + 1 < result.size()) {
            result[i + 1] += result[i] / 10;
            result[i] %= 10;
        }
    }

    while (result.size() > 1 && result.back() == 0) {
        result.pop_back();
    }

    for (auto it = result.rbegin(); it != result.rend(); ++it) {
        cout << *it;
    }
    cout << endl;

    return 0;
}