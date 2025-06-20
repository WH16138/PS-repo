import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.min_idx_tree = [0] * (4*self.n)
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.min_idx_tree[node] = (data[start], start)
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            left = self.min_idx_tree[node*2]
            right = self.min_idx_tree[node*2+1]
            if left[0] < right[0]:
                self.min_idx_tree[node] = left
            else:
                self.min_idx_tree[node] = right

    def query(self, l, r, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return (float("inf"),-1)
        if l <= start and end <= r:
            return self.min_idx_tree[node]
        
        mid = (start + end) // 2
        left = self.query(l, r, node*2, start, mid)
        right = self.query(l, r, node*2+1, mid+1, end)
        if left[0] < right[0]:
            return left
        else:
            return right

N = int(input())
A = list(map(int, input().split()))
seg_tree = SegmentTree(A)

prefix_sum = [0] * (N + 1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + A[i-1]

def get_sum(l, r):
    return prefix_sum[r+1] - prefix_sum[l]

def solve(l,r):
    min_value, min_index = seg_tree.query(l, r)
    if min_index < l or min_index > r:
        return 0
    lrsum = get_sum(l, r)
    return max(lrsum*min_value, solve(l, min_index-1), solve(min_index+1, r))

print(solve(0, N-1))