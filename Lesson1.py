MAXINT = 2147483647
def solution(N):
    if not isinstance(N,int):
        raise TypeError('Must be integer')
    if N>MAXINT:
        raise ValueError('Must be smaller than {}'.format(MAXINT))
    if N<1:
        raise ValueError('Must be bigger than 1')
    binary_string = str(bin(N))[2:]
    #print(binary_string)
    a = binary_string.split("1")
    #print(a)
    #print(a[-1])
    if len(a)<=2:
        return 0
    if binary_string[-1]=='0':
        a.pop(-1)
     #   print(a)
    max=0
    for i in range(0,len(a)):
    #    print(len(a[i]))
        if max<len(a[i]):
            max=len(a[i])
    return max