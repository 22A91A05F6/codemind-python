n=int(input())
a=0
b=1
count=0
for i in range(0,n+1):
    c=a+b
    if c==n:
        count=count+1
        break
    a=b
    b=c
if count!=0:
    print("True")
else:
    print("False")