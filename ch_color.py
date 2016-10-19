long=int(input())
file=input()
res=""
aa=1
i=1
t1=-3
cpp=3
change=input()
changeto=input()
while aa==1:
    t1=t1+cpp
    t2=file[t1:t1+cpp]
    if (t2==change):
        t3=changeto
    else:
        t3=t2
    res=res+t3 
    i=i+1
    if i>long:
        aa=0;
        print(res)
    
