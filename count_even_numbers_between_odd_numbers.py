n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    if i!=0 and i!=n-1:
        if lst[i-1]%2!=0 and lst[i+1]%2!=0:
              c=c+1
print(c)