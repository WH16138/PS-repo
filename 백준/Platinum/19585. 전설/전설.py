import sys
input = sys.stdin.readline

C,N = map(int,input().split())

color = set(input().strip() for _ in range(C))
name = set(input().strip() for _ in range(N))

class Trie():
    def __init__(self):
        self.children = {}
        self.is_end = False
    def insert(self, name):
        node = self
        for char in name:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True
    def check(self, team):
        node = self
        for i in range(len(team)):
            char = team[i]
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_end and team[i+1:] in name:
                return True
        return False
    
trie = Trie()

for c in color:
    trie.insert(c)

query = int(input())
for q in range(query):
    team = input().strip()
    if trie.check(team):
        print("Yes")
    else:
        print("No")