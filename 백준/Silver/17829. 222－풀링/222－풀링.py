N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def solution(n, r, c):
    if n == 2:
        return sorted([arr[r][c], arr[r][c+1], arr[r+1][c], arr[r+1][c+1]])[2]
    else:
        temp = []
        temp.append(solution(n//2, r, c))
        temp.append(solution(n//2, r, c + n//2))
        temp.append(solution(n//2, r + n//2, c))
        temp.append(solution(n//2, r + n//2, c + n//2))
        return sorted(temp)[2]

print(solution(N, 0, 0))