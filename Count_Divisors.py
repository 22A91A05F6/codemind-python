a,b,c=map(int,input().split())
p=0
for i in range(a,b+1):
    if i%c==0:
        p=p+1
print(p)
