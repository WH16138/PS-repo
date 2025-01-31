def selection_sort(A,k):
    n = len(A)
    last = n-1
    while last > 0:
        max_index = A.index(max(A[:last+1]))
        if max_index!= last:
            k -= 1
            if k == 0:
                return (A[last], A[max_index])
            A[last], A[max_index] = A[max_index], A[last]
        last -= 1
    return [-1]

N,K = map(int,input().split())

A = list(map(int,input().split()))

print(*selection_sort(A, K))