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
    
    def query_down(self, l, r, val, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            idx = bisect.bisect_left(self.tree[node], val)
            return idx
        
        mid = (start + end) // 2
        left = self.query_down(l, r, val, node*2, start, mid)
        right = self.query_down(l, r, val, node*2+1, mid+1, end)
        return left + right

n = int(input())
A_map = {}
one = list(map(int, input().split()))
two = list(map(int, input().split()))
for i,v in enumerate(one):
    A_map[v] = i
A_index = [A_map[v] for v in two]

mst = MergeSortTree(A_index)
a = 0
for i,v in enumerate(two):
    a += mst.query_down(i, n-1, A_map[v])
print(a)