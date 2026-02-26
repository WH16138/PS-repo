import sys
import math
from bisect import bisect_right, bisect_left, insort
input = sys.stdin.readline

class SqrtDecomp:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.Bsize = int(math.sqrt(self.n)) + 1
        self.num_blocks = (self.n+self.Bsize-1)//self.Bsize

        self.blocks = []
        for b in range(self.num_blocks):
            l = b * self.Bsize
            r = min(self.n, (b+1) * self.Bsize)
            block = sorted(self.arr[l:r])
            self.blocks.append(block)

    def update(self, idx, val):
        b = idx//self.Bsize
        old = self.arr[idx]
        self.arr[idx] = val

        block = self.blocks[b]

        pos = bisect_left(block, old)
        block.pop(pos)

        insort(block, val)

    def query_count_greater(self, l, r, k):
        bl = l//self.Bsize
        br = r//self.Bsize
        ans = 0

        if bl == br:
            for i in range(l, r + 1):
                if self.arr[i] > k:
                    ans += 1
            return ans
        
        end_left = (bl+1)*self.Bsize - 1
        for i in range(l, end_left+1):
            if self.arr[i] > k:
                ans += 1

        for b in range(bl+1, br):
            block = self.blocks[b]
            ans += len(block) - bisect_right(block, k)

        start_right = br * self.Bsize
        for i in range(start_right, r+1):
            if self.arr[i] > k:
                ans += 1
        return ans

N = int(input())
arr = list(map(int, input().split()))
sd = SqrtDecomp(arr)

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, l, r, k = q
        l -= 1
        r -= 1
        print(sd.query_count_greater(l, r, k))
    else:
        _, i, v = q
        i -= 1
        sd.update(i, v)