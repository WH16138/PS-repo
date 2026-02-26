import sys
input = sys.stdin.readline

class Lazy_SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4*self.n)
        self.lazyA = [0] * (4*self.n)
        self.lazyD = [0] * (4*self.n)
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)

    def apply(self, node, A, D):
        self.lazyA[node] += A
        self.lazyD[node] += D

    def query(self, idx, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        self.propagate(node, start, end)
        
        if start == end:
            return self.tree[node]
        
        mid = (start + end) // 2
        if idx <= mid:
            return self.query(idx, node*2, start, mid)
        else:
            return self.query(idx, node*2+1, mid+1, end)
    
    def propagate(self, node, start, end):
        A = self.lazyA[node]
        D = self.lazyD[node]

        if A == 0 and D == 0:return
        
        if start == end:
            self.tree[node] += A
        else:
            m = (start + end) // 2
            self.apply(node*2, A, D)
            self.apply(node*2+1, A + D*(m-start+1), D)

        self.lazyA[node] = 0
        self.lazyD[node] = 0

    def update_range(self, l, r, node=1, start=0, end=None):
        if end is None:
            end = self.n-1

        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.apply(node, start-l+1, 1)
            return
        
        self.propagate(node, start, end)

        mid = (start + end) // 2
        self.update_range(l, r, node*2, start, mid)
        self.update_range(l, r, node*2+1, mid+1, end)

n = int(input())
arr = list(map(int, input().split()))
st = Lazy_SegmentTree(arr)

for i in range(int(input())):
    cmd, *args = map(int, input().split())
    if cmd == 1:
        st.update_range(args[0]-1, args[1]-1)
    else:
        print(st.query(args[0]-1))