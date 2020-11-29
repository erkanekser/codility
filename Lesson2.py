def solution(A, K):
    tup_A = tuple(A)
    for _ in range(K):
        for i, n in enumerate(tup_A):
            if i < len(A)-1:
                A[i+1] = n
            else:
                A[0] = n
        tup_A = tuple(A)
    return A
    