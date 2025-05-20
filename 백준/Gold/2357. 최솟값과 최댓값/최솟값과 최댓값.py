import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.minTree = [0] * (4*self.n)
        self.maxTree = [0] * (4*self.n)
        self.build(data, 1, 0, self.n-1)
    
    def build(self, data, node, start, end):
        if start == end:
            self.minTree[node] = data[start]
            self.maxTree[node] = data[start]
        else:
            mid = (start+end)//2
            self.build(data, node*2, start, mid)
            self.build(data, node*2+1, mid+1, end)
            self.minTree[node] = min(self.minTree[node*2],self.minTree[node*2+1])
            self.maxTree[node] = max(self.maxTree[node*2],self.maxTree[node*2+1])

    def query(self, l, r, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if r < start or end < l:
            return 1e10, -1e10
        if l <= start and end <= r:
            return self.minTree[node], self.maxTree[node]
        
        mid = (start + end) // 2
        left = self.query(l, r, node*2, start, mid)
        right = self.query(l, r, node*2+1, mid+1, end)
        return min(left[0],right[0]), max(left[1],right[1])
    
    def update(self, idx, val, node=1, start=0, end=None):
        if end is None:
            end = self.n-1
        if start == end:
            self.minTree[node] = val
            self.maxTree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, node*2, start, mid)
            else:
                self.update(idx, val, node*2+1, mid+1, end)
            self.minTree[node] = self.minTree[node*2] + self.minTree[node*2+1]
            self.maxTree[node] = self.maxTree[node*2] + self.maxTree[node*2+1]

N,M = map(int,input().split())
numbers = [int(input()) for i in range(N)]

st = SegmentTree(numbers)
for i in range(M):
    a,b = map(int,input().split())
    print(*st.query(a-1,b-1))