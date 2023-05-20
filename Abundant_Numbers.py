n=int(input())
s=0
i=1
for i in range(1,n):
     if n%i==0:
          s=s+i
if s>n:
    print("True")
else:
    print("False")