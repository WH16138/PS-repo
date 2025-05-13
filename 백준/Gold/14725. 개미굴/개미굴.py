class Trie():
    def __init__(self):
        self.trie = {}
    def MakeSub(self, seq):
        if len(seq) == 0:
            return
        else:
            node:Trie = self.trie.get(seq[0], Trie())
            node.MakeSub(seq[1:])
            self.trie[seq[0]] = node
    def Show(self, f):
        if len(self.trie) == 0: return
        keys = sorted(list(self.trie.keys()))
        for k in keys:
            print(f+k)
            self.trie[k].Show("--"+f)

n = int(input())
T = Trie()
for _ in range(n):
    ipt = input().split()
    k, food = ipt[0], ipt[1:]
    T.MakeSub(food)

T.Show("")