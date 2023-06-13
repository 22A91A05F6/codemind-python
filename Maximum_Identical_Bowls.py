n=int(input())
lst=list(map(int,input().split()))
p=sum(lst)
while p:
    if p%n==0:
        print(n)
        break
    n-=1