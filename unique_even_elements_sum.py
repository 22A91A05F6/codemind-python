n=int(input())
lst=set(map(int,input().split()))
c=0
d=list(lst)
for i in range(len(d)):
    if d[i]%2==0:
         c=c+d[i]
print(c)