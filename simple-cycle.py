# Поиск простых чисел от одного до i

import math; 
q=int(input())
def simple(n):
    res=n
    if n>20:
       op=int(math.sqrt(n+1))
    else:
        op=n
    for i in range(2,op):
        o=n%i
        if(o==0):
            res=""
    print (res)
for l in range(1,q):
    simple(l)
