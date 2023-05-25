n=int(input())
lst=list(map(int,input().split()))
s=0
a,b=map(int,input().split())
for i in range(n):
     if  a<=lst[i] and b>=lst[i]:
           s=s+lst[i]
print(s)
     