n=int(input())
i=1
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
        i=i+1
if sum==n:
    print("True")
else:
    print("False")