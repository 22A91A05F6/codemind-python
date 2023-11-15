
n=int(input())
for i in range(1,n+1):
    p=input()
    temp=p
    n=len(p)
    ki=n%2
    t=""
    for i in p:
        t=i+t
    if p==t and ki==0:
        print("YES EVEN")
    elif p==t and ki!=0:
        print("YES ODD")
    else: 
        print("NO")