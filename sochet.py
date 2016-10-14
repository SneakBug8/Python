def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
    
def sochet(n,k):
    t1=fact(n)
    t2=fact(k)
    t3 = n - k
    t4=fact(t3)
    res=t1/(t2*t4)
    return res

sochet(5,1)
