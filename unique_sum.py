n=int(input())
lst=set(map(int,input().split()))
c=0
d=list(lst)
for i in range(len(d)):
      c=c+d[i]
print(c)