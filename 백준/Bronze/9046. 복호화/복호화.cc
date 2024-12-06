#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    cin.ignore();

    for (int t = 0; t < T; t++) {
        string input;
        getline(cin, input);

        vector<int> freq(26, 0);

        for (char c : input) {
            if (isalpha(c)) {
                freq[c - 'a']++;
            }
        }

        int maxFreq = *max_element(freq.begin(), freq.end());
        int countMax = count(freq.begin(), freq.end(), maxFreq);

        if (countMax > 1) {
            cout << '?' << endl;
        } else {
            char mostFrequent = 'a' + distance(freq.begin(), find(freq.begin(), freq.end(), maxFreq));
            cout << mostFrequent << endl;
        }
    }
    return 0;
}
