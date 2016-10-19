long=3
file="001005101"
res=""
aa=1
i=1
t1=-3
change="001"
changeto="100"
while aa==1:
    t1=t1+3
    t2=file[t1:t1+3]
    if (t2==change):
        t3=changeto
    else:
        t3=t2
    res=res+t3 
    print (res)
    i=i+1
    if i>long:
        aa=0;
    
