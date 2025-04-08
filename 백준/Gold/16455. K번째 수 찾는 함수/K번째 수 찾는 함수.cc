#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int select_kth(vector<int>& a, int left, int right, int k) {
    if(right - left <= 5) {
        sort(a.begin() + left, a.begin() + right);
        return a[left + k];
    }
    
    int numMedians = 0;
    for (int i = left; i < right; i += 5) {
        int groupEnd = min(i + 5, right);
        sort(a.begin() + i, a.begin() + groupEnd);
        int medianIndex = i + (groupEnd - i - 1) / 2;
        swap(a[left + numMedians], a[medianIndex]);
        numMedians++;
    }
    int medianOfMedians = select_kth(a, left, left + numMedians, numMedians / 2);
    
    int pivot = medianOfMedians;
    int lt = left, i = left, gt = right - 1;
    while(i <= gt) {
        if(a[i] < pivot) {
            swap(a[lt++], a[i++]);
        } else if(a[i] > pivot) {
            swap(a[i], a[gt--]);
        } else {
            i++;
        }
    }
    
    int leftCount = lt - left;
    int equalCount = gt - lt + 1;
    if(k < leftCount)
        return select_kth(a, left, lt, k);
    else if(k < leftCount + equalCount)
        return pivot;
    else
        return select_kth(a, gt + 1, right, k - leftCount - equalCount);
}

int kth(vector<int>& a, int k) {
    return select_kth(a, 0, a.size(), k - 1);
}