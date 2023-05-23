n=int(input())
lst=list(map(int,input().split()))
s=0
p=0
for i in range(0,n):
    if i%2==0:
        s=s+lst[i]
for i in range(0,n):
    if i%2!=0:
        p=p+lst[i]
d=s-p
if d==0:
    print("YES")
else:
    print("NO")