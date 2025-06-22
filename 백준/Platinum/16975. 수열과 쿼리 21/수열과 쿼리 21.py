import sys
input = sys.stdin.readline

class Lazy_SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4*self.n)
        self.lazy = [0] * (4*self.n)
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            self.tree[node] = self.tree[node*2] + self.tree[node*2+1]
    
    def propagate(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node*2] += self.lazy[node]
                self.lazy[node*2+1] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, l, r, val, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        self.propagate(node, start, end)

        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.lazy[node] = val
            self.propagate(node, start, end)
            return

        mid = (start + end) // 2
        self.update_range(l, r, val, node*2, start, mid)
        self.update_range(l, r, val, node*2+1, mid+1, end)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def peek(self, idx, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        self.propagate(node, start, end)

        if start == end:
            return self.tree[node]
        
        mid = (start + end) // 2
        if start <= idx <= mid:
            return self.peek(idx, node*2, start, mid)
        else:
            return self.peek(idx, node*2+1, mid+1, end)

N = int(input())
arr = list(map(int,input().split()))

st = Lazy_SegmentTree(arr)
M = int(input())
for _ in range(M):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l, r, v = q[1]-1, q[2]-1, q[3]
        st.update_range(l, r, v)
    elif q[0] == 2:
        idx = q[1]-1
        print(st.peek(idx))