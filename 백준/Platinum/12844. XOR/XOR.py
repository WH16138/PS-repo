import sys
input = sys.stdin.readline
write = sys.stdout.write

class Xor_Lazy_SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 4 * self.n
        self.tree = [0] * self.size
        self.lazy = [0] * self.size
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build(data, node * 2, start, mid)
            self.build(data, node * 2 + 1, mid + 1, end)
            self.tree[node] = self.tree[node * 2] ^ self.tree[node * 2 + 1]

    def propagate(self, node, start, end):
        if self.lazy[node] != 0:
            if (end - start + 1) % 2:
                self.tree[node] ^= self.lazy[node]

            if start != end:
                self.lazy[node * 2] ^= self.lazy[node]
                self.lazy[node * 2 + 1] ^= self.lazy[node]

            self.lazy[node] = 0

    def update_range(self, l, r, val, node=1, start=0, end=None):
        if end is None:
            end = self.n - 1
        self.propagate(node, start, end)

        if r < start or end < l:
            return

        if l <= start and end <= r:
            self.lazy[node] ^= val
            self.propagate(node, start, end)
            return

        mid = (start + end) // 2
        self.update_range(l, r, val, node * 2, start, mid)
        self.update_range(l, r, val, node * 2 + 1, mid + 1, end)
        self.tree[node] = self.tree[node * 2] ^ self.tree[node * 2 + 1]

    def query(self, l, r, node=1, start=0, end=None):
        if end is None:
            end = self.n - 1
        self.propagate(node, start, end)

        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left = self.query(l, r, node * 2, start, mid)
        right = self.query(l, r, node * 2 + 1, mid + 1, end)
        return left ^ right


n = int(input())
arr = list(map(int, input().split()))
st = Xor_Lazy_SegmentTree(arr)

m = int(input())
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, l, r, k = q
        st.update_range(l, r, k)
    else:
        _, l, r = q
        write(str(st.query(l, r))+'\n')