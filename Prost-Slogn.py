n=int(input())
import math; 

res="Simple"
    if n>20:
       op=int(math.sqrt(n+1))
    else:
        op=n
    for i in range(2,op):
        o=n%i
        if(o==0):
            res="Not simple"
    print (res)
