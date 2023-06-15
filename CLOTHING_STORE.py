n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j and lst[i]==lst[j] and lst[i]!=0 and lst[j]!=0:
            c+=1
            lst[i]=0
            lst[j]=0
print(c)       