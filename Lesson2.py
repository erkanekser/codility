MAXINT = 100
MININT = 0
MAXINT_Values = 1000
MININT_Values = -1000

def solution(A: list, K: int):
    if not isinstance(A,list):
        raise TypeError('A must be list')
    if not A:
        raise RuntimeError('A cant be empty.')
    if K > MAXINT or K < MININT:
        raise ValueError('K must be between 0 and 100')
    if len(A) > MAXINT or len(A) < MININT:
        raise ValueError('N must be between 0 and 100')
    for i in A:
        if i < MININT_Values or i > MAXINT_Values:
            raise ValueError('Values must be between -1000 and 1000')
        if not isinstance(i,int):
            raise TypeError('Values must be an integer')
    temp_first=0
    temps_last=0
    for i in range(0,K):
        A.insert(0,A[-1])
        #print(A)
        A.pop(-1)
        #print(A)
    return A

solution(A,K)