# Наименьшее общее кратное WIP
n1 = int(input())
n2 = int(input())
n = 0

while n==0:
    t1=n1%n2
    if t1==0:
        if n1>n2:
            print(n1)
        elif n2>n1:
            print(n2)
        break
    elif n1>n2:
        n1=t1
    elif n2>n1:
        n2=t1
