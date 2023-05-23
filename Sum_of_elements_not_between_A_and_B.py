n=int(input())
lst=list(map(int,input().split()))
s=0
a,b=map(int,input().split())
for i in range(0,n):
    if lst[i]<a or lst[i]>b:
        s=s+lst[i]
print(s)   
    
    