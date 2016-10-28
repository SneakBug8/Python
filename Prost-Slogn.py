n=int(input())
import math; 
res="Simple"
for i in range(2,int(math.sqrt(n+1))):
    o=n%i
    if(o==0):
        res="Not simple"
print (res)
