import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.oddTree = [0]*(4*self.n)
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.oddTree[node] = 1 if data[start] % 2 == 1 else 0
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            self.oddTree[node] = self.oddTree[node*2] + self.oddTree[node*2+1]

    def query(self, l, r, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.oddTree[node]
        
        mid = (start + end) // 2
        left = self.query(l, r, node*2, start, mid)
        right = self.query(l, r, node*2+1, mid+1, end)
        return left+right
    
    def update(self, idx, val, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if start == end:
            self.oddTree[node] = 1 if val % 2 == 1 else 0
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, node*2, start, mid)
            else:
                self.update(idx, val, node*2+1, mid+1, end)
            self.oddTree[node] = self.oddTree[node*2] + self.oddTree[node*2+1]

N = int(input())
arr = list(map(int, input().split()))
st = SegmentTree(arr)
M = int(input())

for _ in range(M):
    q, l, r = map(int, input().split())
    if q == 1:
        st.update(l-1, r)
    elif q == 2:
        print((r - l + 1) - st.query(l-1, r-1))
    elif q == 3:
        print(st.query(l-1, r-1))