n=int(input())
z=len(str(n))
x=0
for i in range(z):
    if(n%10>x):
       x=n%10
       n=n//10
    else:
        n=n//10
print(x)
    