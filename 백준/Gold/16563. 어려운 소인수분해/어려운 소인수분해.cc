#include <bits/stdc++.h>
using namespace std;

vector<int> sieve_of_eratosthenes(int n) {
    vector<bool> prime(n + 1, true);
    vector<int> res;
    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }
    for (int p = 2; p <= n; p++) {
        if (prime[p]) res.push_back(p);
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<int> primes = sieve_of_eratosthenes((int)sqrt(5000000));
    for (int num : nums) {
        vector<int> factors;
        for (int prime : primes) {
            if ((long long)prime * prime > num) break;
            while (num % prime == 0) {
                factors.push_back(prime);
                num /= prime;
            }
        }
        if (num > 1) factors.push_back(num);
        for (int i = 0; i < (int)factors.size(); i++) {
            if (i) cout << " ";
            cout << factors[i];
        }
        cout << "\n";
    }
}