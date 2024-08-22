n = int(input())

words = [input() for _ in range(n)]
dp = {}
def solve(last,use):
    key = f"{last}:{''.join(map(str,use))}"
    if key not in dp:
        a = [0]
        for i,u in enumerate(use):
            if not u and words[i][0] == last:
                new = use[:]
                new[i] = 1
                a.append(solve(words[i][-1],new)+len(words[i]))
        dp[key] = max(a)
    return dp[key]

answer = []
for i in range(n):
    answer.append(solve(words[i][-1],[1 if i==j else 0 for j in range(n)])+len(words[i]))

print(max(answer))