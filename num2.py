x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x=float(input())
y=float(input())
res=""
if (y>y1) and (y>y2):
    res=res+"N"
if (y<y1) and (y<y2):
    res=res+"S"
if (x<x1) and (x<x2):
    res=res+"W"
if (x>x1) and (x>x2):
    res=res+"E"
print (res)
