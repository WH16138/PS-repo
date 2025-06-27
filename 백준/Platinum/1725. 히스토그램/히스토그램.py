import sys
input = sys.stdin.readline

def solution(histo:list):
    if len(histo) == 1:
        return histo[0]
    elif len(histo) == 2:
        return max(min(histo)*2, *histo)
    else:
        mid = len(histo) // 2
        left = solution(histo[:mid])
        right = solution(histo[mid:])
        result = max(left, right)
        
        l,r = mid,mid
        minh = min(histo[l],histo[r])
        while True:
            if 0 < l:
                if r < len(histo)-1:
                    if histo[l-1] > histo[r+1]:
                        l -= 1
                    else:
                        r += 1
                else:
                    l -= 1
            elif r < len(histo)-1:
                r += 1
            else:
                break
            minh = min(minh, histo[l], histo[r])
            result = max(result, minh*(r-l+1))
        
        return result

n = int(input())
histogram = list(int(input()) for _ in range(n))
print(solution(histogram))