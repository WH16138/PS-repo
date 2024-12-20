#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    int n,m,a,b,p,q;
    for (int i = 0; i < T;i++){
        cin >> n >> m;
        vector<long long> pluspoint(n);
        vector<long long> minuspoint(n);
        vector<double> result(n);

        for (int j = 0; j < m; j++)
        {
            cin >> a >> b >> p >> q;
            pluspoint[a-1] += p;
            minuspoint[a-1] -= q;
            pluspoint[b-1] += q;
            minuspoint[b-1] -= p;
        }
        
        for (int j = 0; j < n; j++)
        {
            if (minuspoint[j]==0 && pluspoint[j]==0)
            {
                result[j] = 0;
                continue;
            }
            result[j] = (double) pow(pluspoint[j],2) / (pow(pluspoint[j],2) + pow(minuspoint[j],2));
        }

        cout << (long long)(*max_element(result.begin(), result.end())*1000) << endl;
        cout << (long long)(*min_element(result.begin(), result.end())*1000) << endl;
    }
}