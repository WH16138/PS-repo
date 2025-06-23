import bisect
import sys
input = sys.stdin.readline

class MergeSortTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [[] for _ in range(4*self.n)]
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = [data[start]]
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            self.tree[node] = sorted(self.tree[node*2] + self.tree[node*2+1])

    def query_up(self, l, r, val, node=1, start=0, end=None): # count of elements > val
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            idx = bisect.bisect_right(self.tree[node], val)
            return len(self.tree[node]) - idx
        
        mid = (start + end) // 2
        left = self.query_up(l, r, val, node*2, start, mid)
        right = self.query_up(l, r, val, node*2+1, mid+1, end)
        return left + right

N = int(input())
arr = list(map(int, input().split()))
mst = MergeSortTree(arr)
M = int(input())

ans = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    i, j, k = a^ans, b^ans, c^ans
    ans = mst.query_up(i-1, j-1, k)
    print(ans)