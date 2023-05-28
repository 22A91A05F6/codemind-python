n=int(input())
lst=list(map(int,input().split()))
b=n//2
s=0
p=0
for i in range(0,b):
    s=s+lst[i]
for i in range(b,n):
    p=p+lst[i]
print(s)
print(p)